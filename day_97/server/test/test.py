import json, time
import requests


with open("../prod.json", mode='r') as f:
    data = json.load(f)

url = "http://127.0.0.1:5000"


json_ = {
    "email" : "jhuncarlomacdon@gmail.com",
    "password" : "..."
}

response = requests.post(url=f"{url}/api/auth/" , json=json_)
response.raise_for_status()

token = response.json()['token']


headers = {
    "Authorization" : f"Bearer {token}"
}

for item in data["products"]:
    product = {
        "name" : item["title"],
        "description" : item["description"],
        "price" : item["price"],
        "stock" : item["stock"]
    }

    
    response = requests.post(url=f"{url}/api/products/", headers=headers, json=product)
    response.raise_for_status()

    print(response)