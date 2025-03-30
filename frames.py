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
#driver.switch_to.frame("courses-iframe") name/id/webelement of the iframe
#driver.switch_to.default_content()

driver.find_element(By.XPATH,"//a[@class='btn btn-theme btn-sm btn-min-block']").click()
time.sleep(2)
