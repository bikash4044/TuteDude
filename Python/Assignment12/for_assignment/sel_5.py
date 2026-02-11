
from selenium import webdriver
from selenium.webdriver.common.by import By  # 1. Import 'By'
import time
driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']" ).send_keys("iphone")
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']" ).click()

time.sleep(2)
l = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
print(len(l), " products found")
for i in l:
    print(i.text)
print("Browser is open. Press Enter in this terminal to close it...")
input()