from dotenv import load_dotenv
import smtplib
import os

load_dotenv()


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.email_key = os.getenv("EMAIL_KEY")
        self.email = os.getenv("EMAIL")
        
    def send_alerts(self, to_addrs, messages):
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.email, password=self.email_key)
                msg_1 = f"Subject: Low prices alert too for amazon"
                msg_2 = f"{messages}"
                connection.sendmail(from_addr=self.email, to_addrs=to_addrs,  msg=msg_1 + msg_2)
                return True
        except Exception as e:
            print(e)
            return False   
    
