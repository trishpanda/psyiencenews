from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.nature.com/nature/articles')

soup = BeautifulSoup(page.content, features="lxml")

articles = soup.findAll("article")

data = []
for article in articles:
    time = article.find("time").getText()
    headline = article.find("a", {"data-track-label" : "link"}).getText().splitlines()[2]
    data.append([time, headline])
    print(time + ": " + headline)

    