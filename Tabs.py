import time
import requests
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import javascript
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get("https://testautomationpractice.blogspot.com/")
# driver.switch_to.new_window("window")
driver.get("https://amazon.in/")
# driver.save_screenshot(os.getcwd()+ "\\sample.png")

ck=driver.get_cookies()
print(len(ck))

for c in ck:
    print(c.get('name'), (c.get('value'), (c.get('expiry_date'))))


time.sleep(2)

# Update the Chrome options to run in Headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
