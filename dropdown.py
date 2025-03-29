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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
d_down=Select(driver.find_element(By.XPATH,"//select[@id='country']"))

'''
d_country=Select(d_down)
d_country.select_by_visible_text("India")
d_country.select_by_index(3)
time.sleep(2)
'''

# dropdown_all=d_down.options
# print(len(dropdown_all))
# for dps in dropdown_all:
#     if  dps.text=="India":
#         dps.click()
#         break



