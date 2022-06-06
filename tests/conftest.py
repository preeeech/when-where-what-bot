import pytest
from utils.geocode import GeoBuilder


@pytest.fixture
def event_url():
    return 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRbQUZgHKwbKsigjyK3XKK-pjr53sFPNJ3RRtbP_gtA2uBAl-sN2_KPVLE7FMJk-bUYFUtOZU34L-kZ/pub?gid=935924829&single=true&output=csv'


@pytest.fixture
def geo(event_url):
    return GeoBuilder(event_url)


@pytest.fixture
def origin():
    return "Perth, Australia"


@pytest.fixture
def destinations():
    return [
            "Uluru, Australia",
            "Kakadu, Australia",
            "Blue Mountains, Australia",
            "Bungle Bungles, Australia",
            "The Pinnacles, Australia",
        ]