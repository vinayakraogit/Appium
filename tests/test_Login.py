import pytest
import sys
import os

from conftest import setup_logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.capabilities import create_driver
from pages.login_page import LoginPage


@pytest.fixture(scope="module")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

logger = setup_logging()

def test_login(driver):
    logger.info("Starting Login")
    login_page = LoginPage(driver)
    login_page.login("rakshith.u@spurtreetech.com", "Kalwe@777")
    login_page.handle_permissions()
    login_page.wait_for_sync()
    # login_page.handle_visit()
    logger.info("Ending login")




