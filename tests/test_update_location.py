import time
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.capabilities import create_driver
from pages.navbar_page import Navbar
from pages.menu_page import Menu
from pages.accounts_page import Accounts
from pages.selectedaccount_page import Selectedaccount
from pages.updatelocation_page import Updatelocation


@pytest.fixture(scope="module")
def driver():
    driver = create_driver()
    yield driver


def test_updatelocation(driver): #___chnged from test_update_location to test_updatelocation
    print("In location ")
    navbar_obj = Navbar(driver)  # Create an instance of navbar
    navbar_obj.menu_click()  # Click on menu
    # logging.log.info('menu button click')

    print("Updating Location")

    menu_obj = Menu(driver)
    menu_obj.accounts_click()  # Click on accounts

    time.sleep(1)

    accounts_obj = Accounts(driver)
    accounts_obj.firstaccount_click()

    time.sleep(1)

    selectedaccount_obj = Selectedaccount(driver)
    selectedaccount_obj.kabab_menu_click()
    #selectedaccount_obj.checkin_click()

    time.sleep(1)

    updatelocation_obj = Updatelocation(driver)

    updatelocation_obj.geolocation_click()

    time.sleep(1)

    updatelocation_obj.update_click()
    updatelocation_obj.done_click()



