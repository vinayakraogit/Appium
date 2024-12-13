import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Stockatoutlet:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)


        # Locators
        # self.kabab_menu = (By.XPATH,"//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]")
        self.addmore = (By.ACCESSIBILITY_ID, ", Add More")
        self.searchbar = (By.XPATH, "//android.widget.EditText[@text='Search SKU']")
        self.clickitem = (By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup")
        self.quantity = (By.XPATH, "//android.widget.EditText[@text='0']")
        self.continuebutton = (By.ACCESSIBILITY_ID, "Continue")

    # def kabab_menu_click(self):
    #   self.wait.until(EC.element_to_be_clickable(self.kabab_menu)).click()

    def addmore_click(self):
        self.wait.until(EC.element_to_be_clickable(self.addmore)).click()

    def seachbar_click(self):
        self.wait.until(EC.element_to_be_clickable(self.searchbar)).send_keys('bira')

    def clickitem_click(self):
        self.wait.until(EC.element_to_be_clickable(self.clickitem)).click()

    def quantity_send(self):
        self.wait.until(EC.element_to_be_clickable(self.quantity)).send_keys('1')

    def continuebutton_click(self):
        self.wait.until(EC.element_to_be_clickable(self.continuebutton)).click()







