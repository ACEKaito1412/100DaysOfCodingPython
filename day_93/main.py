from bs4 import BeautifulSoup

text = ""
with open('website.html', mode='r', encoding="utf8") as f:
    text = f.read()

soup = BeautifulSoup(text, "html.parser")

list_title = soup.find_all(name="h2", class_="search-card-e-title")
list_price = soup.find_all(name="div", class_="search-card-e-price-main")
min_order = soup.find_all(name="div", class_="search-card-m-sale-features margin-bottom-4")


with open("data.csv", mode="w") as f:
    text = "item,price,min_order\n"
    for i in range(len(list_title)):
        min_order_ = min_order[i].find(name="div", class_="search-card-m-sale-features__item tow-line")
        text += f"{list_title[i].getText()},{list_price[i].getText()},{min_order_.getText()}\n"
    f.write(text)