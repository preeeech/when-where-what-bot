from utils.geocode import GeoBuilder
import argparse
import os
import sys
import click
import json


with open('links.json') as f:
    default_link = json.load(f)['links']['june5']


@click.command()
@click.argument('origin', default="Austin")
@click.argument('start', default="5:00pm")
@click.argument('end', default="10:00pm")
@click.argument('link', default=default_link)
def main(link, origin, start, end):
    geo = GeoBuilder(link)
    fastest_path = geo.get_fastest_route(origin, time_range=[start, end])
    print(f'Optimal Route:\n{fastest_route}')


if __name__ == '__main__':    
    main()
    