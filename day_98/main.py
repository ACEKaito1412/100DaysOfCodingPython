from bs4 import BeautifulSoup


text = ""
with open('web.html', mode='r', encoding="utf8") as f:
    text = f.read()

soup = BeautifulSoup(text, "html.parser")

list_title = soup.find_all(name="span", class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6")
list_price = soup.find_all(name="span", class_="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u")
list_location = soup.find_all(name="span", class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84")
list_milage = soup.find_all(name="span", class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84")
list_image_uri = soup.find_all(name="img", class_="x15mokao x1ga7v0g x16uus16 xbiv7yw xt7dq6l xl1xv1r x6ikm8r x10wlt62 xh8yej3")


# for item in list_image_uri:
#     print(item['src'])


with open("data.csv", mode="w", encoding='utf8') as f:
    text = "item,price,location,milage,image_uri\n"
    for i in range(len(list_price)):
        try :
             title = list_title[i].getText()

             if title.find("rs")
             text += f"{list_title[i].getText()},{list_price[i].getText()},{list_location[i].getText()},{list_milage[i].getText()},{list_image_uri[i]['src']}\n"
        except Exception as e:
            print("Error occured, skipping data ..")
            pass

    f.write(text)
    print("Done..")