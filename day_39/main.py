#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_m = DataManager()
fs = FlightSearch()

sheet_data = data_m.sheet_data

for item in sheet_data:
    if item['iataCode'] == "":
        iataCode = fs.search_flights(item['city'])
        item['iataCode'] = iataCode

for item in sheet_data:
    data_m.update_data(item_data=item)
