from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')

data = response.text

soup = BeautifulSoup(data, 'html.parser')

article_links = []
article_tags = []


all_articles = soup.find_all(name="span", class_="titleline")

for article in all_articles:
    article_links.append(article.a['href'].strip(''))
    article_tags.append(article.text.strip(''))

subtexts = soup.find_all(name="td", class_="subtext")
article_scores = []

for subtext in subtexts:

    score_tag = subtext.find(name="span", class_="score")
    if score_tag:
        score = int(score_tag.get_text().split()[0])
        article_scores.append(score)
    else:
        article_scores.append(0)

biggest_score = max(article_scores)
index_max_score = article_scores.index(biggest_score)
article_link = article_links[index_max_score]
article_tag = article_tags[index_max_score]

print(f'The article with {biggest_score} upvotes is:\n Link: {article_link} \n Subject: {article_tag}')



















#with open("website.html") as file:
    #html_data = file.read()

#soup = BeautifulSoup(html_data, "html.parser")
#
#print(soup.title.string)
#
#anchor_tags = soup.find_all(name="a")
#print(anchor_tags)
#
#for tag in anchor_tags:
#    print(tag.get("href"))
#
#heading = soup.find(name="h1",id="name")
#print(heading)
#
#section_heading = soup.find(name="h3", class_="heading")
#print(section_heading.get_text())
#
#name = soup.select_one(selector="#name")
#print(name)
#
#headings = soup.select(".heading")
#print(headings)