import requests
from bs4 import BeautifulSoup


URL = "https://www.billboard.com/charts/hot-100/"

class BillBoardData():
    def __init__(self):
        self.html_text = self.get_from_prev_html()
        self.data = self.parse_text()
        self.date = "2013-01-01"

    def get_from_prev_html(self) -> str: 
        with open("web.txt", mode="r", encoding="utf8") as f:
            content = f.read()

        if content == None:
            return ""
        else:
            return content
        
    def get_new_html(self):
        self.date = input("What year do you want to travel to? YYYY-MM-DD: ")
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

        res = requests.get(url=f"{URL}/{self.date}", headers=header)
        res.raise_for_status()

        self.html_text = res.text
        self.data = self.parse_text()
        

    def parse_text(self):
        soup = BeautifulSoup(self.html_text, "html.parser")

        titles_soup = soup.select(selector="li #title-of-a-story")
        singers_soup = [item.find_next() for item in titles_soup]

        singers = [item.getText().strip() for item in singers_soup]
        titles = [item.getText().strip() for item in titles_soup]

        return {'singers' : singers, 'titles' : titles}
