class FlightData:
    def __init__(self, price, origin_airport_code, destination_airport_code, out_date, return_date,stops):
        self.price = price
        self.origin = origin_airport_code
        self.destination = destination_airport_code
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops
    
def find_cheapest_flight(flights_data):

    if len(flights_data) == 0:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = flights_data[0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    stops = len(first_flight["itineraries"])

    print(stops)
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops)

    for flight in flights_data:
        price = float(flight['price']['grandTotal']) 
        if price < lowest_price:
            lowest_price = flight['price']['grandTotal']
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][-1]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            stops = len(first_flight["itineraries"])



    return cheapest_flight
