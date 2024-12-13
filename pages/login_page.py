from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        # Locators
        self.username_field = (By.XPATH, "//android.widget.EditText[@resource-id='username']")
        self.password_field = (By.XPATH, "//android.widget.EditText[@resource-id='password']")
        self.login_button = (By.XPATH, "//android.widget.Button[@resource-id='Login']")
        self.allow_button = (By.XPATH, "//android.widget.Button[@text=' Allow ']")
        self.sync_progress_text = (By.XPATH, "//android.widget.TextView[@text='Sync in Progress']")

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located(self.username_field)).send_keys(username)
        self.wait.until(EC.presence_of_element_located(self.password_field)).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    def handle_permissions(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.allow_button)).click()
        except:
            print("Permission dialog not displayed.")
    def wait_for_sync(self):
        try:
            progressBar = self.wait.until(EC.presence_of_element_located(self.sync_progress_text))
            while progressBar:
                try:
                    progressBar = self.driver.find_element(*self.sync_progress_text)
                    if progressBar.is_displayed():
                        continue
                    else:
                        break
                except:
                    break
        except:
            print("Sync in Progress text not found within timeout.")