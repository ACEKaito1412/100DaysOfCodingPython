import requests
from flight_search import FlightSearch

ENDPOINT = "https://api.sheety.co/952a8c555b507ce7b7d3ead3adab81b8/flightDeals"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = self.get_data()
        self.user_data = self.get_user_data() 
    
    def get_data(self):
        url = f"{ENDPOINT}/prices"
        res = requests.get(url=url)
        data = res.json()['prices']
        return data
    
    def get_user_data(self):
        url = f"{ENDPOINT}/users"

        res = requests.get(url=url)
        data = res.json()['users']
        return data

    
    def update_data(self, item_data):
        url = f"{ENDPOINT}/prices"
        json_params = {
            'price' : {
                'city' : item_data['city'],
                'iataCode' : item_data['iataCode'],
                'lowestPrice' : item_data['lowestPrice']
            }
        }

        res = requests.put(url=f"{url}/{item_data['id']}", json=json_params)
        res.raise_for_status()
        # data = res.json()
        # print(data)
