from selenium import webdriver
from time import sleep
import pyautogui

DINO_LINK = "https://elgoog.im/dinosaur-game/"


driver = webdriver.Chrome() 
driver.get(DINO_LINK)
driver.fullscreen_window()


sleep(5)
pyautogui.press('space')

while True:
    # x, y = pyautogui.position()
    # print(f"mouse : {x} : {y}")

    pixel_color = pyautogui.pixel(520, 903)
    if pixel_color == (83,83,83) or pixel_color == (172,172,172) :
        pyautogui.press('space')
        print(pixel_color)
        # driver.quit()
