class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image
        
class ArticleFetcher():

    
    def fetch(self):
        web_url = "http://python.beispiel.programmierenlernen.io/index.php"
        time.sleep(1)
        print(web_url)
        r = requests.get(web_url)
        doc = BeautifulSoup(r.text, "html.parser")
        
        articles = []
        for i in range(2):
            if len(articles) == 0:
                for card in doc.select(".card"):
                    emoji = card.select_one(".emoji").text
                    content = card.select_one(".card-text").text
                    title = card.select(".card-title span")[1].text
                    image = urljoin(web_url, card.select_one("img").attrs["src"])

                    crawled = CrawledArticle(title, emoji, content, image)
                    articles.append(crawled)

            else:
                # bessere Lösung möglich? ev. len()?
                for a in range(6):
                    for url in doc.find_all('a', href = True):
                        new_url = urljoin(web_url,url.get('href'))

                    r = requests.get(new_url)
                    doc = BeautifulSoup(r.text, "html.parser")


                    for card in doc.select(".card"):
                        emoji = card.select_one(".emoji").text
                        content = card.select_one(".card-text").text
                        title = card.select(".card-title span")[1].text
                        image = urljoin(web_url, card.select_one("img").attrs["src"])

                        crawled = CrawledArticle(title, emoji, content, image)
                        articles.append(crawled)



        return articles
