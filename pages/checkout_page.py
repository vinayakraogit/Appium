from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.todays_visit = (By.ACCESSIBILITY_ID, "Today's Visit (0)")
        self.end_day_button = (By.XPATH, "//android.widget.TextView[@text='End Day']")
    def close_visit(self) :
        self.wait.until(EC.element_to_be_clickable(self.todays_visit)).click()
        self.wait.until(EC.element_to_be_clickable(self.end_day_button)).click()