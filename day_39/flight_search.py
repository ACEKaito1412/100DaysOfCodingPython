import requests

ENPOINT = "https://test.api.amadeus.com/v1"
TOKEN_REQUEST = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = ""
        self.api_secret = ""
        self.api_token = self.get_new_token()

    def get_new_token(self):
        header = {
            "content-type" : "application/x-www-form-urlencoded"
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }

        res = requests.post(url=TOKEN_REQUEST, headers=header, data=body)
        res.raise_for_status()
        
        data = res.json()
        return data['access_token']


    def search_flights(self, search_city):
        url = f"{ENPOINT}/reference-data/locations/cities"

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
        return data['data'][0]['iataCode']