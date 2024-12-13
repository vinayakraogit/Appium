import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.capabilities import create_driver
from pages.login_page import LoginPage
from pages.checkout_page import Checkout
from test_login import test_login
@pytest.fixture(scope="module")
def driver():
    driver = create_driver()
    yield driver
    # driver.quit()
def test_visit_out(driver):
    # Assuming test_login fixture ensures successful login
    checkout_page = Checkout(driver)
    checkout_page.close_visit()
if __name__ == "__main__":
    pytest.main()