import math
import os
import time
from distutils.command.config import config
import pytest
from pages.demoqa_home_page import DemoqaHomePage
from pages.demoqa_elements_page import DemoqaElementsPage
from base.webdriver_setup import WebDriverSetup
from utilities.logger import get_logger
from utilities.screenshot_util import capture_screenshot  # Import the screenshot utility
from pages.demoqa_widgets_page import DemoqaWidgetsPage
from config import settings

logger = get_logger()
trace_path = os.path.join(settings.TRACE_PATH, "trace.zip")



@pytest.fixture(scope="function")
def browser():
    """
    Fixture to initialize and yield a Playwright browser instance using WebDriverSetup.
    """
    browser_instance = WebDriverSetup.get_browser(browser="chrome", headless=False)
    yield browser_instance
    browser_instance.close()

@pytest.fixture(scope="function")
def page(browser):
    """
    Fixture to create and yield a new browser context and page instance ,start and stop tracing.
    """
    context = WebDriverSetup.get_context(browser)
    page = context.new_page()
    page.context.tracing.start(screenshots=True, snapshots=True)
    yield page
    context.close()


def test_home_page(page):
    """
    Test the Home Page for DemoQA.
    """
    logger.info("Starting test for Home Page")
    home_page = DemoqaHomePage(page)  # Pass Playwright's page object
    home_page.load()  # Navigate to the home page
    logger.info("Loaded Home Page")
    try:
        # Validate the page title
        assert "DEMOQA" in home_page.get_title(), "Page title mismatch"
        logger.info("Test passed")
    except AssertionError as e:
        # Capture a screenshot on failure
        logger.error(f"Test failed, screenshot captured at check {settings.REPORT_PATH}")
        raise


def test_reach_elements_page(page):
    logger.info("Starting test for Elements Page")
    home_page = DemoqaHomePage(page)
    home_page.load()
    logger.info("Loaded Home Page")
    home_page.click_elements(page)
    logger.info("Loaded Elements Page")
    elements_page = DemoqaElementsPage(page)
    elements_page.click_side_menu_item(page, "Text Box")
    elements_page.type_text(page, "userName", "Ehud Suryano")
    elements_page.type_text(page, "userEmail", "ehud@gmail.com")
    elements_page.type_text(page, "currentAddress", "rishon lezion")
    elements_page.type_text(page, "permanentAddress", "Rishon Lezion")
    elements_page.scroll_to_element("Submit")
    elements_page.click_button(page, "Submit")
    time.sleep(3)
    try:
        assert "https://demoqa.com/text-box" in elements_page.get_url(), "Page title mismatch"
        logger.info("Test passed")
        assert elements_page.is_element_exist("#output") is True, "can't find output"
        logger.info("output exists")
    except AssertionError as e:
        # Capture screenshot on failure
        capture_screenshot(page, "failure-home-page")
        logger.error("Test failed, screenshot captured")
        raise


def test_reach_widgets_page(page):
    logger.info("Starting test for Elements Page")
    home_page = DemoqaHomePage(page)
    home_page.load()
    logger.info("Loaded Home Page")
    home_page.click_widgets(page)
    logger.info("Loaded Widgets Page")
    widgets_page = DemoqaWidgetsPage(page)
    widgets_page.scroll_to_element("Select Menu")
    widgets_page.click_side_menu_item("Select Menu")
    time.sleep(3)
    try:
        assert "https://demoqa.com/select-menu" in widgets_page.get_url(), "Page title mismatch"
        logger.info("Test passed")
    except AssertionError as e:
        # Capture screenshot on failure
        capture_screenshot(page, "failure-home-page")
        logger.error("Test failed, screenshot captured")
        raise

