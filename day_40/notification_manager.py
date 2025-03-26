from dotenv import load_dotenv
from flight_data import FlightData
import smtplib
import os

load_dotenv()


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email_key = os.getenv("EMAIL_KEY")
        self.email = os.getenv("EMAIL")
        
    def send_alerts(self, to_addrs, cheap_flight: FlightData):
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.email_key)
                msg_1 = f"Subject: Low prices alert too {cheap_flight.destination}\nLow price alert! Only £{cheap_flight.price} to fly from {cheap_flight.origin} to {cheap_flight.destination}\n"
                msg_2 = f"with {cheap_flight.stops} stop(s) departing on {cheap_flight.out_date} and returning on {cheap_flight.return_date}."
                connection.sendmail(from_addr=self.email, to_addrs=to_addrs,  msg=msg_1 + msg_2)
                return True
        except Exception as e:
            return False   
    
