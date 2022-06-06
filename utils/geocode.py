import googlemaps
import os
import itertools
import pandas as pd


class GeoBuilder:
    def __init__(self, spreadsheet_link):
        self.gmaps = googlemaps.Client(key=os.environ['g_key'])
        self.base_url = "https://www.google.com/maps/place/{},{}"
        self.variable_base_url = "https://www.google.com/maps/dir/"
        self.df = pd.read_csv(spreadsheet_link, encoding='utf-8', on_bad_lines='skip')
        self.filter_df(self.df)


    def filter_df(self, df):
        self.df = self.df.drop('RSVP?', axis=1)
        self.df = self.df.drop('Details', axis=1)
        self.df["start"] = self.df["Time"].map(lambda x: self.parse_times(x))
        self.df["end"] = self.df["Time"].map(lambda x: self.parse_times(x, start=False))
        self.df = self.df.dropna()
        self.df["start"] = self.df["start"].map(lambda x: self.add_minutes(x))
        self.df["end"] = self.df["end"].map(lambda x: self.add_minutes(x))
        self.df['start'] = pd.to_datetime(self.df['start'], errors='coerce').dt.time
        self.df['end'] = pd.to_datetime(self.df['end'], errors ='coerce').dt.time
        
        
    def parse_times(self, time_range, start=True):
        if type(time_range) != str:
            return pd.NA
        ampm = ['am', 'pm']
        chars = [str(x) for x in range(0, 10)] + ampm
        times = [x for x in time_range.split('-') if x != '']

        if len(times) > 2:
            return pd.NA
    
        if len(times) == 2:
            valid_start = any([True if char in times[0] else False for char in chars])
            valid_end = any([True if char in times[1] else False for char in chars])

            if not valid_start and not valid_end:
                return pd.NA

            if start and valid_start:
                time = times[0].split()[0]
                if 'am' in time or 'pm' in time:
                    return time
                if 'am' in times[1] or 'pm' in times[1]:
                    return time + 'am' if 'am' in times[1] else time + 'pm'
                else:
                    return pd.NA
    
            if start and not valid_start:
                if valid_end:
                    time = times[1].split()[0]
                    if 'am' in time or 'pm' in time:
                        return time
                    if 'am' in times[0] or 'pm' in times[0]:
                        return time + 'am' if 'am' in times[0] else time + 'pm'
                    else:
                        return pd.NA

            if not start and valid_end:
                time = times[1].split()[0]
                if 'am' in time or 'pm' in time:
                    return time
                if 'am' in times[0] or 'pm' in times[0]:
                    return time + 'am' if 'am' in times[0] else time + 'pm'
                else:
                    return pd.NA

            if not start and not valid_end:
                if valid_start:
                    time = times[0].split()[0]
                    if 'am' in time or 'pm' in time:
                        return time
                    if 'am' in times[1] or 'pm' in times[1]:
                        return time + 'am' if 'am' in times[1] else time + 'pm'
                    else:
                        return pd.NA
                
        if len(times) == 1:
            valid = any([True if char in times[0] else False for char in chars])
            if valid:
                time = times[0].split()[0]
                if 'am' in time or 'pm' in time:
                    return time
                else:
                    return pd.NA
            else:
                return pd.NA

        if len(range) == 0:
            return pd.NA


    def add_minutes(self, time):
        if ':' in time:
            return time
        if 'am' in time:
            return time.split('am')[0] + ':00am'
        if 'pm' in time:
            return time.split('pm')[0] + ':00pm'
        raise Exception('cannot add minutes')


    def get_coordinates(self, location: str):
        '''
        Returns a tuple of coordinates (lat, long) given a location
                Parameters:
                        location (str): a physical location
                Returns:
                        coordinates (tuple): latitude and longitude coordinates
        '''
        gmaps = googlemaps.Client(key=os.environ['g_key'])
        geocode_result = gmaps.geocode(location)
        location = geocode_result[0]['geometry']['location']
        return (location['lat'], location['lng'])


    def build_url(self, lat, long):
        '''
        Returns a Google Maps URL given latitude and longitude
                Parameters:
                        lat (str): latitude of location
                Returns:
                        long (str): longitude of location
        '''
        return self.base_url.format(lat, long).strip()


    def get_fastest_route(self, origin: str, destinations: list = None, time_range: list = None):
        """
        given a starting origin and a list of destinations, 
        return the path with the fasest travel time 
        that covers all destinations from the origin
        """
        if time_range:
            start, end = time_range
            start = pd.to_datetime(start).time()
            end = pd.to_datetime(end).time()
            destinations = self.df[(self.df['start'] >= start) & (self.df['end'] <= end)] 
            destinations = list(destinations['Location'])
        else:
            destinations = list(self.df['Location']) if destinations is None else destinations
        perms = list(itertools.permutations(destinations))
        path_times = {(origin, ) + k: 0 for k in perms}

        for destinations in perms:
            for i, destination in enumerate(destinations):
                starting = destinations[i - 1] if i > 0 else origin
                matrix = self.gmaps.distance_matrix([starting], [destination])
                travel_time = matrix['rows'][0]['elements'][0]['duration']['value']
                path_times[(origin, ) + destinations] += travel_time

        fastest_route = min(path_times, key=path_times.get)
        url = self.variable_base_url
        for destination in fastest_route:
            url += f'{destination}/'

        return url
    