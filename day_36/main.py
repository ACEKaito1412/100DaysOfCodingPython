import requests
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_key = os.getenv("ALPHAVANTAGE_API_KEY")
news_key = os.getenv("NEWS_API_KEY")
email_key = os.getenv("EMAIL_KEY")
email = os.getenv("EMAIL")

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
params_stock = {
    'function' : 'TIME_SERIES_DAILY',
    'symbol' : STOCK_NAME,
    'apikey' : stock_key
}

response = requests.get(url=STOCK_ENDPOINT, params=params_stock)
response.raise_for_status()

stock_data = response.json()['Time Series (Daily)']
closing_data = [value['4. close'] for (key, value) in stock_data.items()]

close_one = float(closing_data[0])

#TODO 2. - Get the day before yesterday's closing stock price

close_two = float(closing_data[1])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = round(close_one - close_two, 2)

if difference < 0:
    difference *= -1

print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage = round((difference / close_one) * 100, 2)
print(percentage)

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

def check_news():
    params_news = {
        'q' : COMPANY_NAME,
        'searchIn' : 'title,description',
        'pageSize' : 3,
        'apiKey' : news_key
    }
    response_new = requests.get(url=NEWS_ENDPOINT, params=params_news)
    response_new.raise_for_status()

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    news_data = response_new.json()['articles'][:3]
    
    return news_data

 
def sendArticle(title, content):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=email_key)
        msg = f"Subject: News about {COMPANY_NAME}\n\n{title}\n{content}"
        connection.sendmail(from_addr=email, to_addrs=email,  msg=msg)


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
article = []
if percentage > 5:
    news_data = check_news()

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    article = [{'headline':key['title'],'description': key['content']} for key in news_data]

    #TODO 9. - Send each article as a separate message via Twilio.
    for item in article:
        sendArticle(item['title'], item['description'])



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


