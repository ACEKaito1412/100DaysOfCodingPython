from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")

list_title = soup.find_all(name="a", class_="storylink")
list_score = soup.find_all(name="span", class_="score")

scores = []
hrefs = []
titles = []
for item in list_title:
    titles.append(item.getText())
    hrefs.append(item.get("href"))

for score in list_score:
    text = int(score.getText().split(" ")[0])
    scores.append(text)

ind = 0
max_point  = 0
for i in range(0, len(list_score)):
    if max_point < scores[i]:
        max_point = scores[i]
        ind = i

print(f"title: {titles[ind]}, link: {hrefs[ind]}, score: {scores[ind]}")


# import lxml

# with open("website.html", mode='r') as f:
#     content = f.read()

# soup = BeautifulSoup(content, "html.parser")

# all_achor_tag = soup.find_all(name="a")


# for tag in all_achor_tag:
#     # print(tag.getText())
#     # getting the attribute link in an anchor tag
#     attr = tag.get('href')
#     print(attr)

# # find a particular element with an id 
# heading = soup.find(name='h1', id="name")
# print(heading)

# # find an element with a class
# section_heading = soup.find(name='h3', class_="heading")
# print(section_heading.getText())

# # using a selector {p a}
# company_url = soup.select_one(selector="p a")
# print(company_url)

# # get a list of a particular element which have that selector
# headings = soup.select(selector=".heading")
# print(headings)

# print(soup.find_all("li"))