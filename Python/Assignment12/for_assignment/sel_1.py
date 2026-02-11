from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.google.com')

search_query = driver.find_element(By.NAME, 'q')
search_query.send_keys('selenium')

search_query.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()