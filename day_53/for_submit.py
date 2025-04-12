from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL_TO_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSeVfel87Dsuxjs4DvrFsmw9XDhE4ekpG1L8Jtu6f6yyLHoXdg/viewform?usp=header"

class SheetSubmit():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        

    def submit(self, data):
        self.driver.get(URL_TO_FORM)

        time.sleep(2)

        in_address = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        in_address.click()
        in_address.send_keys(data['address'])

        time.sleep(1)
        in_price = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        in_price.click()
        in_price.send_keys(data['price'])

        time.sleep(1)
        in_link = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        in_link.click()
        in_link.send_keys(data['link'])

        time.sleep(1)
        btn_submit = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        btn_submit.click()
