#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight, FlightData
from notification_manager import NotificationManager
import time


ORIGIN = "LON"
data_m = DataManager()
fs = FlightSearch()
notif_manager = NotificationManager()

sheet_data = data_m.sheet_data

def send_notification(users, cheap_flight: FlightData, notif_manager : NotificationManager):
    for user in users:
        status = notif_manager.send_alerts(user['email'], cheap_flight)
        if not status:
            print(f"Unable to send mail to {user['email']}")

for item in sheet_data:
    if item['iataCode'] == "":
        iataCode = fs.search_city_code(item['city'])
        item['iataCode'] = iataCode

# for item in sheet_data:
#     data_m.update_data(item_data=item)

for item in sheet_data:
    destination = item['iataCode']
    
    data = fs.search_flights(ORIGIN, destination)

    if data is None:

        data = fs.search_flights(ORIGIN, destination, False)


    cheapest_flight = find_cheapest_flight(data['data'])
    print(f"price: {cheapest_flight.price}")
    
    if cheapest_flight == "N/A" :
        print(f"No flight found for {destination}")
    elif float(cheapest_flight.price) < float(item['lowestPrice']):
        send_notification(data_m.user_data, cheapest_flight)
    else:
        print("skip for now")

    time.sleep(2)

