from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Outletone:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.continueonoutlet = (By.ACCESSIBILITY_ID, 'Continue')
        # self.back = (By.XPATH, '//android.widget.TextView[@text="Check In"]')
    def continueonoutlet_click(self):
        self.wait.until(EC.element_to_be_clickable(self.continueonoutlet)).click()







