from bs4 import BeautifulSoup
import requests

date_travel = input("What year you would like to travel to in YYY-MM-DD format:")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

URL = f"https://www.billboard.com/charts/hot-100/{date_travel}/"

response = requests.get(URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")

song_names_tags = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_tags]

with open ('best 100 songs.txt', 'w', encoding="utf8") as file:
        file.write("\n".join(song_names))