import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.capabilities import create_driver
from pages.checkin_page import Checkin


@pytest.fixture(scope="module")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


def test_visits(driver):
    #  test_login fixture ensures successful login
    checkin_page = Checkin(driver)
    try:

        checkin_page.handle_visit()
    except Exception as e:
        pytest.fail(f"Failed to handle visit: {e}")


print("checkin completed")

# if __name__ == "__main__":
#     pytest.main()
