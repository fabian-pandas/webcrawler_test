import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv


class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image
        
class ArticleFetcher():

    
    def fetch(self):
        web_url = "http://python.beispiel.programmierenlernen.io/index.php"
        articles = []
        with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
            crwld = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
            while web_url !="":
                time.sleep(1)
                print(web_url)
                r = requests.get(web_url)

                 doc = BeautifulSoup(r.text, "html.parser")

                 for card in doc.select(".card"):
                    emoji = card.select_one(".emoji").text
                    content = card.select_one(".card-text").text
                    title = card.select(".card-title span")[1].text
                    image = urljoin(web_url, card.select_one("img").attrs["src"])

                    crawled = CrawledArticle(title, emoji, content, image)
                    articles.append(crawled)

                 next_button = doc.select_one(".navigation .btn") 
                 if next_button:
                    next_href = next_button.attrs["href"]
                    next_href = urljoin(web_url, next_href)
                    print(next_href)
                    web_url = next_href
                else:
                    web_url = ""
        
            for article in articles:
                crwld.writerow([article.emoji,article.title,article.content,article.image])
    
