import pytest
import logging
from selenium import webdriver
from utils.capabilities import create_driver


# Set up logging configuration
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("test_execution.log"),  # Log to a file
            logging.StreamHandler()  # Log to the console
        ]
    )
    return logging.getLogger(__name__)


# Initialize logger
logger = setup_logging()


@pytest.fixture(scope="module")
def driver():
    """Fixture to initialize and quit the WebDriver."""
    logger.info("Initializing WebDriver")
    driver = create_driver()
    yield driver
    logger.info("Quitting WebDriver")
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshots in HTML reports whenever tests fail.
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    pytest_html = item.config.pluginmanager.getplugin('html')

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Ensure driver exists and capture screenshot if possible
            driver = getattr(item.instance, "driver", None)
            if driver:
                file_name = report.nodeid.replace("::", "_") + ".png"
                logger.info(f"Capturing screenshot for failed test: {file_name}")
                try:
                    _capture_screenshot(driver, file_name)
                except Exception as e:
                    logger.error(f"Failed to capture screenshot: {e}")
                html = f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(driver, name):
    try:
        driver.get_screenshot_as_file(name)
        logger.info(f"Screenshot saved as {name}")
    except Exception as e:
        logger.error(f"Could not capture screenshot: {e}")

#__________________________________________________________________________________________________________
# import pytest
# from selenium import webdriver
# from utils.capabilities import create_driver
#
# @pytest.fixture(scope="module")
# def driver():
#     """Fixture to initialize and quit the WebDriver."""
#     driver = create_driver()
#     yield driver
#     driver.quit()
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the PyTest Plugin to take and embed screenshots in HTML reports whenever tests fail.
#     """
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     pytest_html = item.config.pluginmanager.getplugin('html')
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # Ensure driver exists and capture screenshot if possible
#             driver = getattr(item.instance, "driver", None)
#             if driver:
#                 file_name = report.nodeid.replace("::", "_") + ".png"
#                 _capture_screenshot(driver, file_name)
#                 html = f'<div><img src="{file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
#                        f'onclick="window.open(this.src)" align="right"/></div>'
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def _capture_screenshot(driver, name):
#     try:
#         driver.get_screenshot_as_file(name)
#     except Exception as e:
#         print(f"Could not capture screenshot: {e}")
