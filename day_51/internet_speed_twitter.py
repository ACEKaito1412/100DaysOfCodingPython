from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

URL_SPEED_TEST = "https://www.speedtest.net/"
URL_TWITTER = "https://x.com/"
PROMISED_DOWN = 150
PROMISED_UP = 10

class InternetSpeedTwitterBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.chrome_driver = webdriver.Chrome(options=chrome_options)
        self.upload = 0
        self.download = 0
        
    def get_internet_speed(self):
        self.chrome_driver.get(url=URL_SPEED_TEST)
        time.sleep(3)
        go_btn = self.chrome_driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[1]/a')
        go_btn.click()

        state = True

        while state:    
            if self.chrome_driver.current_url != URL_SPEED_TEST:
                time.sleep(3)
                
                self.chrome_driver.save_screenshot('screenshot.png')

                download_element = self.chrome_driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
                upload_element = self.chrome_driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
                
                self.download = float(download_element.text)
                self.upload = float(upload_element.text)

                state = False


    def tweet_at_provider(self):
        self.chrome_driver.get(url=URL_TWITTER)

        if self.download > PROMISED_DOWN or self.upload > PROMISED_UP:
            return
        state = True

        while state:    
            print(self.chrome_driver.current_url)
            if self.chrome_driver.current_url == "https://x.com/home":
                time.sleep(3)
                print("starting")

                post_input_text = self.chrome_driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
                post_input_text.click()
                post_input_text.send_keys(f"Test, Internet speed tweet complaint bot.. ")

                time.sleep(2)
                image_upload = self.chrome_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/nav/div/div[2]/div/div[1]/div/input')
                image_upload.send_keys('C:/Users/ACE/Desktop/Repos/100DaysOfCodingPython/day_51/screenshot.png')
                
                time.sleep(1)
                post_btn = self.chrome_driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
                post_btn.click()
                state = False
            
        
