from exceptions.exceptions import ElementNotFoundException
from handlers import demohqSideMenuItem_Handler
from handlers import textbox_handler
from handlers import button_handler
from utilities.logger import get_logger
from base.base_page import BasePage  # Import the BasePage class

logger = get_logger()


class DemoqaElementsPage(BasePage):  # Inherit from BasePage
    URL = "https://demoqa.com/elements"

    def __init__(self, driver):
        super().__init__(driver)  # Initialize the BasePage with the driver

    def load(self):
        """
        Navigates to the specific page URL.
        """
        self.page.goto(self.URL)  # Use the URL attribute

    def click_side_menu_item(self, driver, item_name):
        try:
            demohqSideMenuItem_Handler.SideMenuItemHandler.on_get_elements(driver, item_name)[0].click()
            logger.info(f"side menu item{item_name}  was clicked")
        except ElementNotFoundException(item_name,timeout = 5):
            logger.error(f"side menu item{item_name} was NOT clicked")
        return

    def type_text(self, driver, text_box, text):
        try:
            textbox_handler.TextboxHandler.on_get_elements(driver, text_box)[0].type(text)
            logger.info(f"{text} was typed into {text_box}")
        except ElementNotFoundException(text_box,timeout = 5):
            logger.error(f"{text} was NOT typed into {text_box}")

    def click_button(self, driver, btn_name):
        try:
            button_handler.ButtonHandler.on_get_elements(driver, btn_name)[0].click()
            logger.info(f"side menu item{btn_name}  was clicked")
        except ElementNotFoundException(btn_name,timeout = 5):
            logger.error(f"side menu item{btn_name} was NOT clicked")
        return
