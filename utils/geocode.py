import googlemaps
import os


class GeoBuilder:
    def __init__(self):
        self.gmaps = googlemaps.Client(key=os.environ['g_key'])
        self.base_url = "https://www.google.com/maps/place/{},{}"

  
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
    