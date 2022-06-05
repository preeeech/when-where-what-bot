import googlemaps
import os
import requests
import pandas as pd
from utils.geocode import GeoBuilder


def scrape_spreadsheet(link):
    res = pd.read_html(link)[0]
    link ='https://docs.google.com/spreadsheets/d/1PUFyF3pq2oDU0gnE1ytaBShB7DGzBLzgy7mlp4QL5jk/edit#gid=935924829'
    


if __name__ == '__main__':
    geo = GeoBuilder()
    coordinates = geo.get_coordinates("902 Monterra Dr, MO")
    link = geo.build_url(*coordinates)
    print(link)
    
  