from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open SauceDemo website
driver.get("https://www.saucedemo.com/")

# Maximize browser window
driver.maximize_window()

# Enter username
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

# Enter password
password = driver.find_element(By.ID, "password")
password.send_keys("wrong_password")

# Click login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Wait for page to load
time.sleep(3)

# Check result
if "inventory" in driver.current_url:
    print("TEST FAILED: Invalid login should not succeed")
else:
    print("TEST PASSED: Invalid login blocked correctly")

# Close browser
driver.quit()
