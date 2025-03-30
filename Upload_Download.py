import time
import requests
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import javascript

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID, "singleFileInput").send_keys(r"C:\Users\Sinergia\Downloads\Surya Resume-1.pdf")
time.sleep(3)

# Set preferences for Chrome options
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": r"C:\Users\Sinergia\Downloads"}  # Replace with your desired download location
chrome_options.add_experimental_option("prefs", prefs)

# Reinitialize the driver with the options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://testautomationpractice.blogspot.com/")

driver.save_screenshot("location\\filename")