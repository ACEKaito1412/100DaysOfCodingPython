import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

USER_NAME = "acekaito1412"
TOKEN = os.getenv("PIXELA_API_KEY")
PIXELA_EP = "https://pixe.la/v1/users/"
GRAPH_EP = f"https://pixe.la/v1/users/{USER_NAME}/graphs"
VALUE_EP = f"https://pixe.la/v1/users/{USER_NAME}/graphs/test-graph"

user_params = {
    'token' : TOKEN,
    'username' : USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=PIXELA_EP, json=user_params)
# print(response.json())

graph_config = {"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}

headers = {
    'X-USER-TOKEN' : TOKEN
}

# response = requests.post(url=GRAPH_EP, json=graph_config, headers=headers)
# print(response)
today = datetime.now()
print(today.strftime("%Y%m%d"))

# Adding a new pixel on graph
value_json = {"date": today.strftime("%Y%m%d"),"quantity":"100"}
# res = requests.post(url=VALUE_EP, json=value_json, headers=headers)
# print(res.json())


# Updating data in api
# date = today.strftime("%Y%m%d")
# new_value_json = {"quantity":"5"}
# res = requests.put(url=f"{VALUE_EP}/{date}", json=new_value_json, headers=headers)
# print(res.json())

# removing data in api
# date = today.strftime("%Y%m%d")
# res = requests.delete(url=f"{VALUE_EP}/{date}", headers=headers)
# print(res.json())