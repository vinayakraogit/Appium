from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Accounts:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.search = (By.XPATH, "//android.widget.EditText[@text='Search']")
        self.first_account = (By.XPATH, "//android.widget.TextView[@text='43423-Dakshayini L']")
    def firstaccount_click(self):
        self.wait.until(EC.element_to_be_clickable(self.first_account)).click()