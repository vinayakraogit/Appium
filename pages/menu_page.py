from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Menu:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.accounts = (By.XPATH, '//android.widget.TextView[@text="Accounts"]')
    def accounts_click(self):
        self.wait.until(EC.element_to_be_clickable(self.accounts)).click()





