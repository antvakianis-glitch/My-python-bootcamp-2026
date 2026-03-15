import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")

#pixela_endpoint = "https://pixe.la/v1/users"
#
#user_params = {
#    "token":TOKEN,
#    "username":USERNAME,
#    "agreeTermsOfService":"yes",
#    "notMinor":"yes"
#}
#
#response = requests.post(pixela_endpoint, json=user_params)
#print(response.text)

#graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

#graph_params = {
#    "id":"graph1",
#    "name":"Cycling Graph",
#    "unit": "Km",
#    "type":"float",
#    "color":"sora",
#}

headers = {
    "X-USER-TOKEN":TOKEN,

}

#graph_response = requests.post(graph_endpoint, json=graph_params,headers=headers)
#print(graph_response.text)

current_date = datetime.datetime.now()
string_date = current_date.strftime("%Y%m%d")
km_run = float(input("Type how many km you have covered today:"))


post_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"

post_params = {
    "date":"20260314",
    "quantity":str(km_run)
}

post_response = requests.post(url=post_endpoint, json=post_params, headers=headers)
print(post_response.text)

data = post_response.json()

if data.get("isSuccess"):
    print(f"✅ Bravo! Recorded {km_run} km for today.")
else:
    print(f"❌ Something went wrong. Message Pixela: {data.get('message')}")

#delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/20260314"
#
#delete_response = requests.delete(delete_endpoint, headers=headers)
#print(delete_response.text)

