# Getting the events in python main page

from selenium import webdriver
from selenium.webdriver.common.by import By

url  = "https://www.python.org/"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome()
chrome_driver.get(url=url)

elements = chrome_driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget .shrubbery .menu li")

upcoming_event = {}
for i in range(0, len(elements)):
    element = elements[i]
    time_ = element.find_element(by=By.CSS_SELECTOR, value="time").text
    name_ = element.find_element(by=By.TAG_NAME, value="a").text
    upcoming_event[i] = {'time': time_ , 'name' : name_}

print(upcoming_event)