from twilio.rest import Client
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

lat = os.environ.get("lat")
lon = os.environ.get("lon")

from_number = os.environ.get("from_number")
to_number = os.environ.get("to_number")

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "units": "metric",
    "cnt":4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

weather_ids = [search_item["weather"][0]["id"] for search_item in data["list"]]

if any(int(id_code) < 700 for id_code in weather_ids):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will rain today, bring an umbrella!",
        from_=from_number,
        to=to_number,
    )
    print(f"Status: {message.status}")
else:
    print("Sunny weather today")


