from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class OutletCheckin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.continu = (By.XPATH, '//android.widget.TextView[@text="Continue"]')
        self.back = (By.XPATH, '//android.widget.TextView[@text="Back"]')
    def continue_click(self):
        self.wait.until(EC.element_to_be_clickable(self.continu)).click()