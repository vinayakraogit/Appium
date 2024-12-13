import pytest
import sys
import os

from conftest import setup_logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.capabilities import create_driver
from tests.test_Login import test_login
from tests.test_checkin import test_visits
from tests.test_stock_at_outlet import test_stockat_outlet
from tests.test_update_location import test_updatelocation


@pytest.fixture(scope="module")
def driver():
    driver = create_driver()

    logger = setup_logging()

    logger.info("Starting Login")
    test_login(driver)
    logger.info("Ending Login")

    test_visits(driver)

    test_updatelocation(driver)

    test_stockat_outlet(driver)

    yield driver


if __name__ == "__main__":
    pytest.main()
