import time
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver= webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//input[@id='sunday']").click()

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")

'''
print(len(checkboxes))
for i in range(len(checkboxes)):
    checkboxes[i].click()

#All Boxes
for boxes in checkboxes:
    boxes.click()
    time.sleep(1)

#first 2 boxes
for boxes in checkboxes:
    wname=boxes.get_attribute('id')
    if wname=='sunday' or wname=='monday':
        boxes.click()

#last 2 boxes
for i in range(len(checkboxes)-2, len(checkboxes)):
    checkboxes[i].click()
time.sleep(2)

#first 2 boxes
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()
time.sleep(2)
'''
