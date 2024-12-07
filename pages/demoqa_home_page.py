from playwright.sync_api import sync_playwright
from handlers import card_handler
from utilities.logger import get_logger
from base.base_page import BasePage  # Import the BasePage class

logger = get_logger()


class DemoqaHomePage(BasePage):  # Inherit from BasePage
    URL = "https://demoqa.com"

    def __init__(self, driver):
        super().__init__(driver)  # Initialize the BasePage with the driver

    def load(self):
        """
        Navigates to the specific page URL.
        """
        self.page.goto(self.URL)  # Use the URL attribute

    def click_elements(self, driver):
        try:
            card_handler.CardHandler.on_get_elements(driver, "Elements")[0].click()
            logger.info("Elements card was clicked")
        except Exception("element not found"):
            logger.error("Elements card was NOT clicked")
        return

    def click_widgets(self, driver):
        try:
            card_handler.CardHandler.on_get_elements(driver, "Widgets")[0].click()
            logger.info("Widgets card was clicked")
        except Exception("element not found"):
            logger.error("Widgets card was NOT clicked")
        return