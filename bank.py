from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

import excelutils
from excelutils import ExcelUtils

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(10)
try:
    no_thanks_button = driver.find_element(By.XPATH, "//button[text()='No thanks']")
    ActionChains(driver).move_to_element(no_thanks_button).click().perform()
    print("Pop-up dismissed.")
except Exception as e:
    print(f"No pop-up found. Exception: {e}")

file = r"C:\Users\Sinergia\Desktop\DDTest.xlsx"  # Used raw string to avoid escaping issues
rows = ExcelUtils.getRowCount(file, "Sheet1")
print(f"Number of rows in the sheet: {rows}")

for r in range(2, rows + 1):
    prin = ExcelUtils.readData(file, "Sheet1", r, 1)
    ROI = ExcelUtils.readData(file, "Sheet1", r, 2)
    Pd1 = ExcelUtils.readData(file, "Sheet1", r, 3)
    Pd2 = ExcelUtils.readData(file, "Sheet1", r, 4)
    freq = ExcelUtils.readData(file, "Sheet1", r, 5)
    mv = ExcelUtils.readData(file, "Sheet1", r, 6)

    driver.find_element(By.ID, "principal").clear()
    driver.find_element(By.ID, "principal").send_keys(prin)
    driver.find_element(By.ID, "interest").clear()
    driver.find_element(By.ID, "interest").send_keys(ROI)
    driver.find_element(By.ID, "tenure").clear()
    driver.find_element(By.ID, "tenure").send_keys(Pd1)
    pr = Select(driver.find_element(By.ID, "tenurePeriod"))
    pr.select_by_visible_text(Pd2)
    fq = Select(driver.find_element(By.ID, "frequency"))
    fq.select_by_visible_text(freq)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()

    mv_result = driver.find_element(By.XPATH, "//span[@id='resp_matval']//strong").text

    try:
        if float(mv) == float(mv_result):
            print("Test Passed")
            ExcelUtils.writeData(file, "Sheet1", r, 8, "Passed")
            ExcelUtils.fillGreen(file, "Sheet1", r, 8)
        else:
            print("Test Failed")
            ExcelUtils.writeData(file, "Sheet1", r, 8, "Failed")
            ExcelUtils.fillRed(file, "Sheet1", r, 8)
    except Exception as e:
        print(f"Error during validation: {e}")
        ExcelUtils.writeData(file, "Sheet1", r, 8, "Error")
        ExcelUtils.fillRed(file, "Sheet1", r, 8)

    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
