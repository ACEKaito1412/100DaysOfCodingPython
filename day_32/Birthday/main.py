##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import random as rand
import smtplib
import datetime as dt

LETTERS = ['letter_1.txt', 'letter_2.txt','letter_3.txt']

EMAIL = ""
PASSWORD = ""


# SEND THE LETTER
def email_me(letter, address):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        msg = f"Subject: Happiest Birthday\n\n{letter}"
        connection.sendmail(from_addr=EMAIL, to_addrs=address, msg=msg)

# READ B-DAY LIST

b_day_list = pd.read_csv('birthdays.csv')

# GET THE LIST OF PERSON WHO's B-DAY is TODAY

now = dt.datetime.now()
month_list = b_day_list[(b_day_list['month']) == now.month]
person_list = month_list[month_list['day'] == now.day]

# PICK A LETTER
def random_letter():
    file_path = f"./letter_templates/{rand.choice(LETTERS)}"
    with open(file=file_path, mode='r') as f:
        leter = f.read()

    return leter

# SEND
for _, row in person_list.iterrows():
    new_letter = random_letter()
    new_letter = new_letter.replace("[NAME]", row['name'])
    email_me(letter=new_letter, address=row['email'])