 # "When-Where-What" Optimal Route CLI Tool


## About The Project: 
WhenWhereWhat bot gives the ability to scrape data from spreadsheets containing Austin events and activities. The bot prepares the scraped data and calculates the optimal routes to the destinations in the sheet based on the time frame you specify.

## Links to WhenWhereWhat
* Instagram: https://www.instagram.com/whenwherewhataustin/?hl=en
* Website: https://linktr.ee/whenwherewhataustin
* Example Spreadsheet (June 3rd-5th): https://docs.google.com/spreadsheets/d/1PUFyF3pq2oDU0gnE1ytaBShB7DGzBLzgy7mlp4QL5jk/edit#gid=935924829)
* About WhenWhereWhat Austin: https://www.statesman.com/story/entertainment/2022/03/30/when-where-what-austin-events-feed-instagram-ready-expand-blue-square-things-to-do/6598527001/

### Built With

* [Google Maps](https://github.com/googlemaps/google-maps-services-python)
* [Pandas](https://pandas.pydata.org/)
* [Click](https://click.palletsprojects.com/en/8.1.x/)


<!-- GETTING STARTED -->
## Getting Started

#### installing packages
`pip install -r requirements.txt`

#### getting API key
- get google map API key: https://console.cloud.google.com/apis/credentials

#### injecting API key
- secrets tab (🔒) -> key: 'g_key', value: < API KEY >

<!-- USAGE EXAMPLES -->
## Usage

The CLI tool scrapes events from [when-where-austin](https://linktr.ee/whenwherewhataustin) spreadsheets

`python main.py <spreadsheet link> <origin location> <start time> <end time>`

* example:
`python main.py https://docs.google.com/spreadsheets/d/e/2PACX-1vRbQUZgHKwbKsigjyK3XKK-pjr53sFPNJ3RRtbP_gtA2uBAl-sN2_KPVLE7FMJk-bUYFUtOZU34L-kZ/pub?gid=935924829&single=true&output=csv Austin 4pm 8pm`


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

[@just_PREECHing](https://twitter.com/just_PREECHing) - preechaeamsaart@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>

