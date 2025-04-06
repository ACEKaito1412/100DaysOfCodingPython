from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os
import time as t

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD_1")

url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(chrome_options)
chrome_driver.get(url=url)

t.sleep(5)

wait = WebDriverWait(chrome_driver, 15)
sign_in_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "sign-in-modal__outlet-btn")))

state = True

try:
    sign_in_btn.click()
except Exception as e:
    state = False

    modal_dismiss = chrome_driver.find_element(by=By.CLASS_NAME, value="modal__dismiss")
    modal_dismiss.click()
    print(e.args)

t.sleep(5)

if state:
    email_input = chrome_driver.find_element(By.NAME, value="session_key")
    email_input.send_keys(email, Keys.ENTER)

    pass_input = chrome_driver.find_element(By.NAME, value="session_password")
    pass_input.send_keys(password, Keys.ENTER)


    t.sleep(5)

    easy_apply_btn = chrome_driver.find_element(By.ID, value="jobs-apply-button-id")
    easy_apply_btn.click()

    form_contact = chrome_driver.find_element(By.CSS_SELECTOR, value="form .ph5")
    inputs = form_contact.find_elements(By.TAG_NAME, value="input")

    phone_n = inputs[-1]
    phone_n.send_keys("09774249341")

else:
    print("Exception occurs")