import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        # Κράτα μόνο το base domain εδώ
        self.base_url = "https://kiwi-com-cheap-flights.p.rapidapi.com"
        self.rapidapi_key = os.environ.get("rapidapi_key")
        self.headers = {
            "x-rapidapi-key": self.rapidapi_key,
            "x-rapidapi-host": "kiwi-com-cheap-flights.p.rapidapi.com"
        }

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        # 1. ΠΡΟΣΟΧΗ: Το URL ΠΡΕΠΕΙ να τελειώνει σε /round-trip
        url = "https://kiwi-com-cheap-flights.p.rapidapi.com/round-trip"

        # 2. Τα ονόματα των κλειδιών πρέπει να είναι ΑΚΡΙΒΩΣ όπως τα θέλει ο Scraper
        query = {
            "source": origin_city_code,  # "City:belgrade_rs"
            "destination": destination_city_code,  # "City:paris_fr"
            "currency": "eur",
            "adults": "1",
            "sortBy": "PRICE",
            "outboundDepartmentDateStart": from_time,
            "inboundDepartureDateStart": to_time,
            "limit": "1"
        }

        # Χρησιμοποίησε το search_url εδώ!
        response = requests.get(url=url, headers=self.headers, params=query)

        # Αν σου βγάλει πάλι error, δες τον κωδικό κατάστασης
        if response.status_code != 200:
            print(f"API Error {response.status_code}: {response.text}")

        return response.json()


