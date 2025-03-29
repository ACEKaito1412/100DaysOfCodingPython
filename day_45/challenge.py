from bs4 import BeautifulSoup
import requests

res = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

content = res.text
soup = BeautifulSoup(content, "html.parser")

titles = soup.find_all(name='h3', class_="title")

with open('Movies.txt', mode='w', encoding="utf8") as f:
    for i in range(len(titles) - 1, 0, -1):
        titles_text = titles[i].getText()
        f.write(f"{titles_text}\n")