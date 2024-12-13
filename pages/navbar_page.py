from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Navbar:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.menu = (By.XPATH, "//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.View/android.view.View[6]/android.view.ViewGroup[1]/android.widget.ImageView")
        self.visits = (By.XPATH, '//android.view.View[@content-desc="Visits"]')
        self.orders = (By.XPATH, '//android.view.View[@content-desc="Orders"]')
        self.contacts = (By.XPATH, '//android.view.View[@content-desc="Contacts"]')
        self.POSM = (By.XPATH, '//android.view.View[@content-desc="POSM"]')
    def menu_click(self):
        self.wait.until(EC.element_to_be_clickable(self.menu)).click()

