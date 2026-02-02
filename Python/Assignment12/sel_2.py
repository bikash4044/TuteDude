from selenium import webdriver
from selenium.webdriver.common.by import By  # 1. Import 'By'
import time
driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(5)
# 2. Use the new syntax
input1 = driver.find_element(By.LINK_TEXT, 'Electronics')
input1.click()

time.sleep(2)
input2 = driver.find_element(By.LINK_TEXT, 'Audio')
input2.click()
time.sleep(2)


driver.refresh()
print("Browser is open. Press Enter in this terminal to close it...")
input()