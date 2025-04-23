import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

MAIL = os.getenv('EMAIL')
SMTP_KEY = os.getenv('GMAIL_SMTP_KEY')


def mail_me(subject:str, message:str, to_email_addrs:str):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MAIL, password=SMTP_KEY)
        msg = f"Subject: {subject}\n\n{message}"
        connection.sendmail(from_addr=MAIL, to_addrs=to_email_addrs, msg=msg)
