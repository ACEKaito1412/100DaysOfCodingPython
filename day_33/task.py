import requests
import datetime
import smtplib

MY_LAT = 14.338190
MY_LNG = 120.859284

email = ""
password = "nawkfujkpgudxxpgw"


def email_me():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        msg = f"Subject: ISS Position Overhead\n\nYou should look up."
        connection.sendmail(from_addr=email, to_addrs="catherinedevenecia83@gmail.com", msg=msg)


def get_iss_position():
    res = requests.get(url='http://api.open-notify.org/iss-now.json')
    res.raise_for_status()

    data = res.json()['iss_position']

    latitude  = data['latitude']
    longitude = data['longitude']

    return (float(latitude), float(longitude))

parameters = {
    'lat' : MY_LAT,
    'lng': MY_LNG,
    'formatted' : 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()['results']
sunrise = data['sunrise'].split("T")[1].split(':')[0]
sunset = data['sunset'].split("T")[1].split(':')[0]


print(f"{sunrise} : {sunset}")

now = datetime.datetime.now()
cur_hour = now.hour


if(cur_hour > int(sunset)):
    coor = get_iss_position()

    if MY_LAT - 10 < coor[0]  and coor[0] > MY_LAT + 10 or MY_LNG - 10 < coor[1]  and coor[1] > MY_LNG + 10:
        try:
            email_me()
        except:
            print("Cant sent a message.")