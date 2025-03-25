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
        
    def send_article(self, cheap_flight: FlightData):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.email_key)
            msg_1 = f"Subject: Cheap Flight to {cheap_flight.destination}\n\nDestination: {cheap_flight.destination}\nPrice: {cheap_flight.price}\n"
            msg_2 = f"Out Date: {cheap_flight.out_date}\nReturn: {cheap_flight.return_date}"
            connection.sendmail(from_addr=self.email, to_addrs="macdon.jc.bscs@gmail.com",  msg=msg_1 + msg_2)