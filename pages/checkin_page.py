from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Checkin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.todays_visit = (By.ACCESSIBILITY_ID, "Today's Visit (0)")
        self.start_day_button = (By.XPATH, "//android.widget.TextView[@text='Start Day']")
        self.end_day_button = (By.XPATH, "//android.widget.TextView[@text='End Day']")
        self.confirm_start_day_button = (By.XPATH, "//android.widget.TextView[@text='Yes']")
    def handle_visit(self):
        self.wait.until(EC.element_to_be_clickable(self.todays_visit)).click()
        try:
            self.wait.until(EC.presence_of_element_located(self.end_day_button))
            print("Visit already started")

        except:
            self.wait.until(EC.element_to_be_clickable(self.start_day_button)).click()
            self.wait.until(EC.element_to_be_clickable(self.confirm_start_day_button)).click()
print("Visit started Successfully")#
