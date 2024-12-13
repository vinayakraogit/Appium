import sys
import time
import driver
import ele
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Define capabilities
options = AppiumOptions()
options.set_capability("appium:deviceName", "6h5hnb5dtccm5lcy")
options.set_capability("platformName", "Android")
options.set_capability("appium:automationName", "UIAutomator2")
options.set_capability("appium:appActivity", "com.bira91.beast.MainActivity")
options.set_capability("appium:appPackage", "com.bira91.beast")
options.set_capability("autoGrantPermissions", True)  # Automatically grant all permissions

# Appium server URL
url = "http://localhost:4723"
username = "mohammad.shakeel@spurtreetech.in.preprod"
password = "Kalwe@555"

# Initialize the WebDriver
driver = webdriver.Remote(url, options=options)
wait = WebDriverWait(driver, 20)

# Log in process
wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='username']"))).send_keys(username)
wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='password']"))).send_keys(password)
login_button = driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='Login']")
login_button.click()

# Handle permission dialog if it appears
wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.Button[@text=' Allow ']"))).click()

# Wait for "Sync in Progress" text
progressBar = None
try:
    progressBar = wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Sync in Progress']")))
    print(progressBar.text)
except Exception as e:
    print("Sync in Progress text not found within timeout.")

# Wait until the progress bar is no longer displayed

while progressBar:
    try:
        # Check if the text is still visible and matches
        if progressBar.is_displayed():
            time.sleep(1)  # Optional sleep to avoid constant checking
        else:
            break  # Exit the loop if text is no longer present
    except:
        break  # Exit the loop if the element is not found

# Proceed once the sync process is finished

time.sleep(1)
wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//android.view.ViewGroup[contains(@content-desc, \"Today's Visit\")]"))).click()
time.sleep(1)
try:
    Start_Day = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Start Day"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Yes"))).click()
    print("Visit started Successfully")

except:
    # Wait until the 'End Day' element is present
    if wait.until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, "End Day"))).is_displayed():
        print("Visit already started")

time.sleep(1)

#menu_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.TextView[@text='Menu']")))
menu_button = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Menu")))
menu_button.click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.TextView[@text='Accounts']"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"//android.widget.TextView[@text='43026 Darshan A']"))).click()

#______________Error in clicking 3 dots :,
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]"))).click()
print("clicked on 3dots")
wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Geo Location"))).click()
wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Update"))).click()
wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Done"))).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH,"//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]"))).click()
wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Check In"))).click()
wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Continue"))).click()
wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Continue"))).click()
time.sleep(1)
wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Continue"))).click()
wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, ", Add Contact"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@text='First Name']"))).send_keys('Test')
wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@text='Last Name']"))).send_keys('QA')
wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@text='Phone']"))).send_keys('9164445686')
wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Save"))).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup"))).click()
wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Continue"))).click()
time.sleep(2)




wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, ", Add More"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@text='Search SKU']"))).send_keys('Bira')
wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.ScrollView/android.view.ViewGroup"))).click()



# wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@text='0']"))).send_keys(1)
# wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Continue"))).click()

# wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "Check In"))).click()
    # wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID,"Continue"))).click()




