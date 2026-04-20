from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Add product to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

time.sleep(2)

# Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

time.sleep(2)

# Check if product is in cart
cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

if len(cart_items) > 0:
    print("TEST PASSED: Product added to cart")
else:
    print("TEST FAILED: Product not added")

driver.quit()
