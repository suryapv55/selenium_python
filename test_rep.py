import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHRM:

    @allure.severity(allure.severity_level.NORMAL)
    def test_logo(self):
        """Test to check if the OrangeHRM logo is displayed."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        try:
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

            # Explicit wait for the logo to be visible
            wait = WebDriverWait(self.driver, 10)
            logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div/div[2]/img")))

            assert logo.is_displayed(), "Logo is not displayed!"

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_logo_failure",
                          attachment_type=AttachmentType.PNG)
            pytest.fail(f"Test failed due to: {e}")
        finally:
            self.driver.quit()

    @allure.severity(allure.severity_level.MINOR)
    def test_employees(self):
        """Test is intentionally skipped."""
        pytest.skip("The test is skipped")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        """Test to check login functionality."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        try:
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

            # Explicit waits for elements
            wait = WebDriverWait(self.driver, 10)
            username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']")))

            # Perform login
            username.send_keys("Admin")
            password.send_keys("admin123")
            login_button.click()

            # Verify login success by checking page title
            wait.until(EC.title_contains("OrangeHRM"))
            assert "OrangeHRM" in self.driver.title, "Login success!"

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_failure",
                          attachment_type=AttachmentType.PNG)
            pytest.fail(f"Test failed due to: {e}")
        finally:
            self.driver.quit()
