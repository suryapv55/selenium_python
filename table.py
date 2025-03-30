import time
import requests
from docutils.parsers.rst.directives.misc import Class
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class WebTable:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        self.driver.maximize_window()

# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.XPATH, "//table[@name='courses']")))
    def webtablecount(self,driver):
         n_row=len(driver.find_elements(By.XPATH,"//table[@name='courses']//tr"))
         n_col=len(driver.find_elements(By.XPATH,"//table[@name='courses']//tr[1]/th"))

         print(n_row)
         print(n_col)
#Specific data
# data=driver.find_element(By.XPATH,"//table[@name='courses']//tr[10]/td[2]").text
# print(data)

# ---To print all the values dynamic xpath:
# for r in range(2,n_row+1):
#     for c in range(1,n_col+1):
#         data = driver.find_element(By.XPATH, f"//table[@name='courses']//tr[{r}]/td[{c}]").text
#         print(data, end='    ')
#     print()

#---Specific conditions
# for r in range(2,n_row+1):
#     data1=int(driver.find_element(By.XPATH, f"//table[@name='courses']//tr[{r}]/td[3]").text)
#     if data1>25:
#         course=driver.find_element(By.XPATH, f"//table[@name='courses']//tr[{r}]/td[2]").text
#         print(course,"    ",data1)

wb=WebTable()
wb.webtablecount(wb.driver)
#Dynamic Table -> similar to specific details pick


