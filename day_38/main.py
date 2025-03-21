import requests

APP_ID = "57d5243b"
APP_KEY = "af67fd139ac9ee0eba4218e3f79053cc"

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = "yoga 30 mins"
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




response = requests.post(endpoint, json=parameters, headers=headers)
result = response.json()
print(result)