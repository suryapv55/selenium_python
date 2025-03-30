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

driver= webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.ID,"field1").click()
driver.maximize_window()
act=ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(3)

# Set download preferences
download_path = "C:\\path\\to\\your\\download\\directory"  # Replace with your desired download location
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,  # Disable download prompt
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,  # Enable Safe Browsing
}
options.add_experimental_option("prefs", prefs)

# Initialize the WebDriver with the updated options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Example code to trigger a file download
driver.get("URL_of_the_page_with_file_to_download")  # Replace with your target URL
download_button = driver.find_element(By.ID, "ID_of_download_button")  # Replace with target element
download_button.click()

time.sleep(5)  # Allow time for the download to complete
