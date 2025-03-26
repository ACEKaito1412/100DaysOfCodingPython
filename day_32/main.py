import smtplib
import random
import datetime as dt

email = ""
password = ""

# READ QUOTES TXT
with open("quotes.txt", 'r') as f:
    data = f.readlines()

# MAIL A QOUTE

def email_me():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        msg = f"Subject: Qoute of the day\n\n{random.choice(data).strip()}"
        connection.sendmail(from_addr=email, to_addrs="catherinedevenecia83@gmail.com", msg=msg)


now = dt.datetime.now()

weekday = now.weekday()

if weekday == 6 :
    email_me()

print(now.weekday())