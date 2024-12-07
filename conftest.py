import pytest
import allure
from datetime import datetime
from utilities.screenshot_util import capture_screenshot


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"reports/report_{now}.html"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to check test execution results and capture screenshots for failures.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Check if WebDriver is in test fixture
        driver = item.funcargs.get("driver", None)
        if driver:
            capture_screenshot(driver, f"screenshot-{item.name}")
