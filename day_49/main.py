from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os
import time as t
import random

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD_1")

url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(chrome_options)
chrome_driver.get(url=url)



t.sleep(random.uniform(5,9))

wait = WebDriverWait(chrome_driver, random.uniform(5, 9))
sign_in_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "sign-in-modal__outlet-btn")))

state = True

#  sometimes button is cant be click
try:
    sign_in_btn.click()
except Exception as e:
    state = False
    print("Button Cant be click")

# wait for the page to load
t.sleep(4)

if state:
    # input email and password
    email_input = chrome_driver.find_element(By.NAME, value="session_key")
    email_input.send_keys(email, Keys.ENTER)

    pass_input = chrome_driver.find_element(By.NAME, value="session_password")
    pass_input.send_keys(password, Keys.ENTER)


    t.sleep(random.uniform(5, 9))

    easy_apply_btn = chrome_driver.find_element(By.ID, value="jobs-apply-button-id")
    easy_apply_btn.click()

    form_contact = chrome_driver.find_element(By.CSS_SELECTOR, value="form .ph5")
    inputs = form_contact.find_elements(By.TAG_NAME, value="input")

    phone_n = inputs[-1]
    phone_n.send_keys("09774249341")

    form_footer = chrome_driver.find_element(By.CSS_SELECTOR, value="form footer")
    next_btn = form_footer.find_element(By.TAG_NAME, value="button")
    next_btn.click()

    t.sleep(random.uniform(5,9))

    # review
    form_footer = chrome_driver.find_element(By.CSS_SELECTOR, value="form footer")
    review_btn = form_footer.find_elements(By.TAG_NAME, value="button")

    if review_btn[1].text != "Review":
        review_btn[1].click()
    else:
        t.sleep(2)
        easy_apply_modal = chrome_driver.find_element(by=By.CLASS_NAME, value="jobs-easy-apply-modal")
        buttons = easy_apply_modal.find_elements(By.TAG_NAME, "button")
        
        t.sleep(random.uniform(4,8))
        # exit 
        buttons[0].click()


        confirm_modal = chrome_driver.find_element(by=By.CLASS_NAME, value="artdeco-modal--layer-confirmation")
        confirm_btn = confirm_modal.find_elements(By.TAG_NAME, "button")
        
        t.sleep(random.uniform(4,8))
        # discard
        confirm_btn[1].click()
        print("Skip")

    # submit application
    # form_footer = chrome_driver.find_element(By.CSS_SELECTOR, value="form footer")
    # submit_btn = form_footer.find_element(By.TAG_NAME, value="button")
    # submit_btn.click()


else:
    print("Exception occurs")