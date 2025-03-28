import time

from SeleniumLibrary.keywords import ExpectedConditionKeywords
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


driver= webdriver.Chrome(service = Service(ChromeDriverManager().install()))
'''
driver.implicitly_wait(10)
#Application commands
driver.get("https://testautomationpractice.blogspot.com/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.maximize_window()

#Conditional commands
name_field=driver.find_element(By.ID, "name")
print(name_field.is_displayed())
print(name_field.is_enabled())

male_rb=driver.find_element(By.ID, "male")
fm_rb=driver.find_element(By.ID, "female")
fm_rb.click()
print(male_rb.is_selected())
print(fm_rb.is_selected())

#Browser commands
driver.find_element(By.LINK_TEXT, "merrymoonmary").click()
time.sleep(3)
driver.close()
time.sleep(3)

#Navigational Commands
driver.get("https://amazon.in")
driver.back()
driver.forward()
driver.refresh()
driver.quit()

ele=driver.find_elements(By.XPATH,"//div[@class='widget-content']//a")
print(len(ele))

for e in ele:
    print(e.text)
'''
#find_element vs find_elements
#get_text vs get_attribute_value
#wait_commands
mywait=WebDriverWait(driver,10)

footer_link=mywait.until(EC.presence_of_element_located((By.LINK_TEXT,"By.LINK_TEXT, 'merrymoonmary'")))
footer_link.click()
