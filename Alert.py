import time

import requests
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver= webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
#driver.find_element(By.XPATH,"//*[@id='promptBtn']").click()
# Handle prompt alert
alert = driver.switch_to.alert
alert.accept()
alert.dismiss()
alert_text = alert.text
#print(alert_text)
alert.send_keys("Test Input")
# time.sleep(2)


