from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Correct driver setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Amazon
driver.get("https://www.amazon.in")
time.sleep(3)

search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("iphone 16")
search.send_keys(Keys.RETURN)
time.sleep(3)

price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
print("Amazon Price:", price)

driver.quit()
