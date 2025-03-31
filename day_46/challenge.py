import requests
from bs4 import BeautifulSoup


# url = "https://www.billboard.com/charts/hot-100/"

# date = input("What year do you want to travel to? YYYY-MM-DD: ")

# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# res = requests.get(url=f"{url}/{date}", headers=header)

with open("web.txt", mode="r", encoding="utf8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")

titles_soup = soup.select(selector="li #title-of-a-story")
singers_soup = soup.select(selector="li .c-label")

singers = [item.getText().strip() for item in singers_soup]
titles = [item.getText().strip() for item in titles_soup]
print(f"{titles[0]} : {singers[0]}" )