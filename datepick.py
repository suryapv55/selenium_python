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
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)
driver.find_element(By.ID,"datepicker").click()
driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("04/06/2025")
time.sleep(2)