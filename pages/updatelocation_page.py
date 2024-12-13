import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait


class Updatelocation:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        # Locators

        #self.kabab_menu = (By.XPATH,"//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]")
        self.geolocation_button = (By.ACCESSIBILITY_ID, "Geo Location")
        self.update_button = (By.ACCESSIBILITY_ID, "Update")
        self.done_button = (By.ACCESSIBILITY_ID, "Done")


    def geolocation_click(self):
        self.wait.until(EC.element_to_be_clickable(self.geolocation_button)).click()

    def update_click(self):
        self.wait.until(EC.element_to_be_clickable(self.update_button)).click()

    def done_click(self):
        self.wait.until(EC.element_to_be_clickable(self.done_button)).click()





