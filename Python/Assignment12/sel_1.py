from selenium import webdriver
from selenium.webdriver.common.by import By  # 1. Import 'By'
import time
driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

# 2. Use the new syntax
input_field = driver.find_element(By.NAME, 'field-keywords')
input_field.send_keys("samsung s23 ultra")

# Google's "Google Search" button (btnK) is often not clickable
# instantly because of the autosuggest dropdown.
# Submitting the form via the input field is usually safer:
input_field.submit()

# Alternatively, if you must click the button:
# time.sleep(3) # Wait for overlay to clear
# button = driver.find_element(By.NAME, 'btnK')
# button.click()

time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.quit()

print("Browser is open. Press Enter in this terminal to close it...")
input()