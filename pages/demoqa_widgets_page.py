from playwright.sync_api import sync_playwright
from handlers import demohqSideMenuItem_Handler
from handlers import textbox_handler
from handlers import button_handler
from utilities.logger import get_logger
from base.base_page import BasePage  # Import the BasePage class

logger = get_logger()


class DemoqaWidgetsPage(BasePage):  # Inherit from BasePage
    URL = "https://demoqa.com/elements"

    def __init__(self, page):
        super().__init__(page)  # Initialize the BasePage with the Playwright page object

    def load(self):
        """
        Navigates to the specific page URL.
        """
        self.page.goto(self.URL)  # Use the Playwright `goto` method

    def click_side_menu_item(self, item_name):
        try:
            # Assuming `on_get_elements` returns locators compatible with Playwright
            elements = demohqSideMenuItem_Handler.SideMenuItemHandler.on_get_elements(self.page, item_name)
            elements[0].click()
            logger.info(f"Side menu item '{item_name}' was clicked")
        except Exception as e:
            logger.error(f"Side menu item '{item_name}' was NOT clicked. Error: {e}")
