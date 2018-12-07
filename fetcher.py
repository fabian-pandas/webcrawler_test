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
        
        return articles
    

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
