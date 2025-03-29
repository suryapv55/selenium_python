import time

import requests
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


driver= webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("http://www.deadlinkcity.com/")
#driver.maximize_window()

total_links=driver.find_elements(By.TAG_NAME,"a")
#print(len(total_links))
count=0
#Broken_link
for link in total_links:
    url=link.get_attribute("href")
    try:
        response=requests.head(url)
    except:
        None
    if response.status_code>=400:
        print(url, "is a broken link")
        count+=1

    else:
        print(url, "valid link")
        count+=1

print("total number of broken links:" ,count)
