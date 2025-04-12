from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from for_submit import SheetSubmit
import time

URL_TO_ZILLOW = "https://appbrewery.github.io/Zillow-Clone"

res = requests.get(url=URL_TO_ZILLOW)
res.raise_for_status()

zillow_text = res.text

soup = BeautifulSoup(zillow_text, "html.parser")

element_container = soup.find(name="ul", class_="List-c11n-8-84-3-photo-cards")

list_items = element_container.find_all(name="li")

def clean_price(str_price) -> float:
    str_price = str_price.split(" ")[0]
    n = ""
    for char in str_price:
        
        if char == ".":
            n += char
        elif char.isdigit():
            n += char

    return float(n)

apartment_list = []

for item in list_items:
    el_price = item.find(name='span', class_="PropertyCardWrapper__StyledPriceLine")
    el_address = item.find(name='address')
    el_anchor = item.find(name="a", class_="StyledPropertyCardDataArea-anchor")

    if el_price == None:
        pass
    else:
        href = el_anchor.get('href')
        price = clean_price(el_price.text)
        address = el_address.text.strip()

        apartment_list.append({'price' : price, 'address' : address, "link" : href})


sheet_submit = SheetSubmit()

for apartment in apartment_list:
    try:
        sheet_submit.submit(apartment)
        time.sleep(1.5)
    except Exception as e:
        print("Skip")