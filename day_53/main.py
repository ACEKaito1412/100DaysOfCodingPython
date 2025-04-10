from bs4 import BeautifulSoup
import requests

URL_TO_ZILLOW = "https://appbrewery.github.io/Zillow-Clone"
URL_TO_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSeVfel87Dsuxjs4DvrFsmw9XDhE4ekpG1L8Jtu6f6yyLHoXdg/viewform?usp=header"

res = requests.get(url=URL_TO_ZILLOW)
res.raise_for_status()

zillow_text = res.text

soup = BeautifulSoup(zillow_text, "html.parser")

element_container = soup.find(name="ul", class_="List-c11n-8-84-3-photo-cards")

list_items = element_container.find_all(name="li")

for item in list_items:
    
    price = item.find(name='span', class_="PropertyCardWrapper__StyledPriceLine")
    address = item.find(name='address')
    link_ = item.find(name="a", class_="StyledPropertyCardDataArea-anchor")

    if price == None:
        pass
    else:
        print(f"{price.text.strip()} : {address.text.strip()} : {link_.text.strip()}")