from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://www.amazon.in')
driver.maximize_window()

time.sleep(5)

select = driver.find_element(By.LINK_TEXT, 'Electronics')
select.click()

time.sleep(5)

select_1 = driver.find_element(By.LINK_TEXT, 'Audio')
select_1.click()

time.sleep(5)
driver.quit()