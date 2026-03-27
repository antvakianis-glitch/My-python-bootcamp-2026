import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.sheety_url = os.environ.get("SHEETY_URL")
        self.headers = {
            "Authorization": f"Bearer {os.environ.get("bearer_code")}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.sheety_url, headers=self.headers)
        data = response.json()

        print(f"Sheety Response: {data}")

        self.destination_data = data["prices"]
        return self.destination_data
