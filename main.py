from utils.geocode import GeoBuilder


if __name__ == '__main__':    
    link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRbQUZgHKwbKsigjyK3XKK-pjr53sFPNJ3RRtbP_gtA2uBAl-sN2_KPVLE7FMJk-bUYFUtOZU34L-kZ/pub?gid=935924829&single=true&output=csv'
    geo = GeoBuilder(link)
    fastest_path = geo.get_fastest_route("Austin, TX", time_range=["11:00am", "1:00pm"])
    print(fastest_path)
    