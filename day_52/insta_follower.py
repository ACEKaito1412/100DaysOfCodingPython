from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

URL_TWEETER = "https://x.com/"

class TweeterFollower():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.list_of_following = []
        self.chrome_driver = webdriver.Chrome(options=chrome_options)

    def login(self) -> bool:
        self.chrome_driver.get(url=URL_TWEETER)

        state = True

        while state:

            print(self.chrome_driver.current_url)
            if self.chrome_driver.current_url == "https://x.com/home":
                time.sleep(3)
                self.chrome_driver.get(f"{URL_TWEETER}Google/following/")

                time.sleep(3)
                follow_container = self.chrome_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div')
                
                self.list_of_following = follow_container.find_elements(By.XPATH, "./*")
                state = False
        

    def show_following(self):
        for follow in self.list_of_following:
            a = follow.find_element(By.TAG_NAME, 'a')
            link = a.get_attribute("href")
            print(f"User: {link[13:-1]}")

            
    def follow(self):
        # //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div

        for follow in self.list_of_following:
            time.sleep(random.uniform(2.0, 3.5))
            btns = follow.find_element(By.TAG_NAME, 'button')
            
            # follow user
            btns[1].click()

            a = follow.find_element(By.TAG_NAME, 'a')
            link = a.get_attribute("href")
            print(f"Followed {link[13:-1]}")
