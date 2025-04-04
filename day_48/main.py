from selenium import webdriver
from selenium.webdriver.common.by import By

#  Keep browser open
chrome_option = webdriver.EdgeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Edge(options=chrome_option)
driver.get("https://appbrewery.github.io/instant_pot/")


# price_whole = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
# price_fraction = driver.find_element(by=By.CLASS_NAME, value="a-price-fraction")

# print(f"the price is {price_whole.text}.{price_fraction.text}")

# driver.find_element(By.NAME, "fname") # useful for finding inputs in form
# driver.find_element(By.ID, "submitBtn") #finding element using there idd

# driver.find_element(By.CSS_SELECTOR, ".demo_class a") # using css selector

# driver.find_element(By.XPATH, '//*[@id="udemy"]/div[1]/div[2]/footer/div[5]/div/div[2]/ul/li/button/span') #finding element using its element path

# driver.close() this will close the tab that is open
driver.quit() # this will close the browser