import requests
from datetime import datetime
from dotenv import load_dotenv 
import os

load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv("API_KEY")

endpoint_track = "https://trackapi.nutritionix.com/v2/natural/exercise"
endpoint_sheet = "https://api.sheety.co/952a8c555b507ce7b7d3ead3adab81b8/workout/workouts"

query = input("What did you do today: ")
parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 54,
    "height_cm": 154,
    "age": 23
}

headers = {
    'x-app-id' : APP_ID,
    'x-app-key' : APP_KEY
}



response = requests.post(endpoint_track, json=parameters, headers=headers)
result = response.json()
result = result['exercises'][0]


now = datetime.now()

parameters_wrk = {
    'workout' : {
        'date' : now.strftime("%Y/%m/%d"),
        'time' : now.strftime("%H:%M"),
        'exercise' : result['user_input'],
        'duration' : result['duration_min'],
        'calories' :  round(float(result['nf_calories']))
    }
}

headers = {
    'Authorization' : os.getenv("SHEETY_TOKEN")
}

response = requests.post(endpoint_sheet, json=parameters_wrk, headers=headers)
result = response.json()
print(result)