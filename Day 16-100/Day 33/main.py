import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(f"ISS is at: {latitude}, {longitude}")

