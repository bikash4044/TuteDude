from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

# --- Login ---
# Note: Ensure these selectors match your current Facebook login page version
emailelement = driver.find_element(By.NAME, 'email')
emailelement.send_keys("8260673993")

passelement = driver.find_element(By.NAME, 'pass')
passelement.send_keys("facebookPass@4044")
time.sleep(2)

elem = driver.find_element(By.NAME, 'login')
elem.click()

# Wait for login to complete (Manual input allows you to handle 2FA if needed)
print("Press Enter in the console once fully logged in...")
input()
print("Logged in successfully")

# --- Open "Create Post" Modal ---
# Converted to CSS Selector for better stability with multiple classes
# This clicks the "What's on your mind?" box
post_start = driver.find_element(By.CSS_SELECTOR, '.x1i10hfl.x1ejq31n.x18oe1m7.x1sy0etr.xstzfhl.x972fbf.x10w94by.x1qhh985.x14e42zd.x9f619.x1ypdohk.x3ct3a4.xdj266r.x14z9mp.xat24cr.x1lziwak.x16tdsg8.x1hl2dhg.xggy1nq.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xmjcpbm.x12ol6y4.x180vkcf.x1khw62d.x709u02.x78zum5.x1q0g3np.x1iyjqo2.x1nhvcw1.x1n2onr6.xt7dq6l.x1ba4aug.x1y1aw1k.xpdmqnj.xwib8y2.x1g0dm76')
post_start.click()
time.sleep(5) # Wait for the modal to pop up

# --- Type "1" into the Post (Context from previous turn) ---
# We target the specific paragraph element inside the modal
# Using the class you provided: "xdj266r x14z9mp xat24cr x1lziwak x16tdsg8"
text_area = driver.find_element(By.CSS_SELECTOR, 'p.xdj266r.x14z9mp.xat24cr.x1lziwak.x16tdsg8')

# Click to focus (just in case) then type
text_area.click()
text_area.send_keys("Using Selenium . . .")
time.sleep(5)

# --- Click the Final Post Button ---
post_button = driver.find_element(By.XPATH, "//span[text()='Post']")
driver.execute_script("arguments[0].click();", post_button)
# Keep browser open briefly to verify
time.sleep(5)