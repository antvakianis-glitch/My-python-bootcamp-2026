import datetime
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

BASE_URL = "https://app.100daysofpython.dev"
POST_URL = "/v1/nutrition/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


data_input = input("Enter your today's exercise routine:")

params_data = {
    "query":data_input,
}
try:
    response = requests.post(f"{BASE_URL}{POST_URL}",json=params_data, headers=headers)
    data = response.json()

    print("=" * 60)
    print("API RESPONSE:")
    print("=" * 60)


    print(json.dumps(data, indent=2))
    print("=" * 60)

    print(f"\n✅ Found {len(data['exercises'])} exercise(s):\n")

    current_date = datetime.datetime.now()
    string_date = current_date.strftime("%d/%m/%Y")

    string_time = current_date.strftime("%H:%M:%S")

    sheety_params = {}

    for exercise in data["exercises"]:
        name = exercise.get("name", "Unknown")
        duration = exercise.get("duration_min", 0)
        calories = exercise.get("nf_calories", 0)

        print(f"- {name.title()}: {calories} cal, {duration} min")

        sheety_params = {
            "workout": {
                "date": string_date,
                "time": string_time,
                "exercise": name.title(),
                "duration": duration,
                "calories": calories
            }
        }

        print("\n" + "=" * 60)
        print("DEBUG: Sheety Request")
        print("=" * 60)
        print(f"Body: {sheety_params}")
        print("=" * 60 + "\n")

        sheety_headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

        sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers)

        if sheety_response.status_code == 200:
            print(f"  ✅ Added to Sheety!")
        else:
            print(f"  ❌ Sheety Error: {sheety_response.text}")

    print("\n🎉 All exercises logged!")

except Exception as e:
    print(f"❌ Error: {e}")