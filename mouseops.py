import time
import requests
from docutils.parsers.rst.directives.misc import Class
from pandas.io.formats.format import return_docstring
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import javascript

driver= webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world/")
driver.maximize_window()
#driver.find_element(By.ID,"mousehover").click()
#top=driver.find_element(By.LINK_TEXT,"Top")
#reload=driver.find_element(By.LINK_TEXT,"Reload")
# button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act = ActionChains(driver)
#---mousehover
# act.move_to_element(top).click().perform()
#---right_click
#act.context_click(button).perform()
#---double_click
# act.double_click(button).perform()


#drag_drop and Sliders
# e1=driver.find_element(By.ID,"draggable")
# e2=driver.find_element(By.ID,"droppable")
# act.drag_and_drop(e1,e2).perform()
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print(value)

# country=driver.find_element(By.XPATH,"//a[normalize-space()='Guyana']")
# driver.execute_script("arguments[0].scrollIntoView();",country)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)

