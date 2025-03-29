import time
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver= webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

#window_id=driver.current_window_handle
#print(window_id)

#driver.find_element(By.ID,"openwindow").click()
#w_ids=driver.window_handles

driver.find_element(By.ID,"opentab").click()

ws=driver.window_handles

for w in ws:
    driver.switch_to.window((w))
    print(driver.title)

# child_window=w_ids[1]
# parent_window=w_ids[0]
#
# #print(parent_window,child_window)
# driver.switch_to.window(child_window)
# print(driver.title)
#
# driver.switch_to.window(parent_window)
# print(driver.title)

# for ids in w_ids:
#     driver.switch_to.window(ids)
#     print(driver.title)





