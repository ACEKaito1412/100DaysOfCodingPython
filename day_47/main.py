import requests
from bs4 import BeautifulSoup
from notification_manager import NotificationManager

TO_ADRS = "macdon.jc.bscs@gmail.com"

nf = NotificationManager()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0", 
           "Accept-Language" : "en-US,en;q=0.9"}

url = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
res = requests.get(url=url, headers=headers)
res.raise_for_status()

text = res.text
print(text)
soup = BeautifulSoup(text, "html.parser")

price = soup.find(name="span", class_="aok-offscreen").getText().strip()
price = float(price.replace("$", ""))

messages = f"Low price for your pot at {price}"

if price < 50:
    nf.send_alerts(TO_ADRS, messages=messages)
else:
    print(f"price is {price}: skip for now")