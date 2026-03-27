from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")

all_headers = soup.find_all("h2")

movie_titles = [movie.getText().strip() for movie in all_headers]

movie_list = []

for title in movie_titles:
    if ")" in title:
        movie_list.append(title)

movie_list.reverse()

with open ('movie_list.txt', 'w', encoding="utf8") as file:
    file.write("\n".join(movie_list))
