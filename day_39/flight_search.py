import requests
import datetime
from dotenv  import load_dotenv
import os

load_dotenv()

ENPOINT_V1 = "https://test.api.amadeus.com/v1"
ENPOINT_V2 = "https://test.api.amadeus.com/v2"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv('AMADEUS_KEY')
        self.api_secret = os.getenv('AMADEUS_SECRET')
        self.api_token = self.get_new_token()

    def get_new_token(self):
        url = f"{ENPOINT_V1}/security/oauth2/token"
        header = {
            "content-type" : "application/x-www-form-urlencoded"
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }

        res = requests.post(url=url, headers=header, data=body)
        res.raise_for_status()
        
        data = res.json()
        return data['access_token']


    def search_city_code(self, search_city):
        url = f"{ENPOINT_V1}/reference-data/locations/cities"

        header = {
            'authorization' : f"Bearer {self.api_token}"
        }
        
        params = {
            'keyword' : search_city,
            'max' : 10,
            'include' : "AIRPORTS"
        }

        res = requests.get(url=url, headers=header, params=params);
        res.raise_for_status()

        data = res.json()

        iataCode = data['data'][0]['iataCode']

        if iataCode == "":
            print(f"No iata code for {search_city}")

        return iataCode
    
    def search_flights(self, origin, iataCode):
        url = f"{ENPOINT_V2}/shopping/flight-offers"

        start_date = datetime.datetime.today() + datetime.timedelta(days=1)
        end_date = datetime.datetime.today() + datetime.timedelta(days=91)

        headers = {
            'Authorization' : f"Bearer {self.api_token}"
        }

        query = {
            "originLocationCode": origin,
            "destinationLocationCode": iataCode,
            "departureDate": start_date.strftime("%Y-%m-%d"),
            "returnDate": end_date.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        res = requests.get(url=url, headers=headers, params=query)

        if res.status_code != 200:
            print(f"check_flights() response code: {res.status_code}")
            return None

        data = res.json()

        return data
