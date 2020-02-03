from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.nature.com/search?q=DNA&date_range=last_7_days')

soup = BeautifulSoup(page.content, features="lxml")

headlines = soup.findAll("h2", {"itemprop": "headline"})

data = []
for headline in headlines:
    print(headline.getText().strip() + "\n")

    