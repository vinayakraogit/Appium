import time
import pytest
import sys
import os

from pages.stock_at_outlet_page import Stockatoutlet
from tests.test_Login import test_login
from tests.test_checkin import test_visits
from tests.test_update_location import test_updatelocation


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.capabilities import create_driver

@pytest.fixture(scope="module")
def driver():
    driver = create_driver()
    yield driver

def test_stockat_outlet(driver):
    print("Stock at outlet in progress")

    stockatoutlet_obj = Stockatoutlet(driver)

    # stockatoutlet_obj.kabab_menu_click()

    stockatoutlet_obj.addmore_click()

    stockatoutlet_obj.seachbar_click()

    stockatoutlet_obj.clickitem_click()

    stockatoutlet_obj.quantity_send()

    stockatoutlet_obj.continuebutton_click()

