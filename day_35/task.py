import requests
import os

api_key = os.getenv("OPEN_WEATHER_API_KEY")

LAT = 14.477140
LNG = 120.892242

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    'lat': LAT,
    'lon':LNG,
    'appid': api_key,
    'cnt' : 4
}
response = requests.get(url=endpoint, params=params)
response.raise_for_status()
data = response.json()
print(f"Response:{data['cod']}")

bring_umbrella = False
for item in data['list']:
    weather_id = item['weather'][0]['id']
    if weather_id < 701:
        bring_umbrella = True

if bring_umbrella:
    print("Bring an umbrella")