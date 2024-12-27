import os
import pytest
from datetime import datetime
from utilities.screenshot_util import capture_screenshot
from config import settings


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{settings.REPORT_PATH}/report_{now}.html"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to check test execution results and capture screenshots for failures.
    """
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    trace_path = os.path.join(settings.TRACE_PATH, f"trace_{now}.zip")
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        page = item.funcargs.get("page", None)
        page.context.tracing.stop(path=trace_path)
    if report.when == "call" and report.failed:
        # Check if WebDriver is in test fixture
        page = item.funcargs.get("page", None)
        if page:
            phase = report.when  # e.g., "setup", "call", or "teardown"
            capture_screenshot(page, f"{item.name}")





@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser-name")

def pytest_addoption(parser):
    parser.addoption("--browser-name", default="chromium")