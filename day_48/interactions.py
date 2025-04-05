from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get(url=url)

fname = chrome_driver.find_element(By.NAME, "fName")
fname.send_keys("Ace", Keys.ENTER)

lname = chrome_driver.find_element(by=By.NAME, value="lName")
lname.send_keys("Kaito", Keys.ENTER)

email = chrome_driver.find_element(by=By.NAME, value="email")
email.send_keys("Ace@gmail.com", Keys.ENTER)

btn_submit = chrome_driver.find_element(by=By.CSS_SELECTOR, value="form button")
btn_submit.click()


