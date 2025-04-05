from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time as t
import threading as Thread


state = True

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get(url = "https://orteil.dashnet.org/experiments/cookie/")

cookie_per_sec = chrome_driver.find_element(by=By.ID, value="cps")

cookie_store = chrome_driver.find_element(by=By.ID, value="store")

cookie_btn = chrome_driver.find_element(by=By.ID, value="cookie")

def check_store():
    clickable_item = cookie_store.find_elements(by=By.XPATH, value="//div[@class='']")
    if len(clickable_item):
        last_item = clickable_item[-1]
        last_item.click()

def exit_cookie():
    global state
    print(f"Cookies/S: {cookie_per_sec.text}")
    state = False
    chrome_driver.quit()

check_store()


timeout = t.time() + 5
five_min = t.time() + (60 * 2)

while state:
    cookie_btn.click()

    if t.time() > timeout:
        check_store()

        timeout = t.time() + 5
    
    if timeout > five_min:
        exit_cookie()

