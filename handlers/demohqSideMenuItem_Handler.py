from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from utilities.logger import get_logger
from base.base_handler import BaseHandler
logger = get_logger()


class SideMenuItemHandler(BaseHandler):
    @staticmethod
    def on_get_elements(page: Page, item_name: str, timeout: int = 10000):
        """
        Wait for and return all web elements matching the query.

        :param page: Playwright's Page instance
        :param item_name: String to locate elements (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the elements (default is 10,000 ms)
        :return: List of element handles found using the constructed XPath, or an empty list if none are found
        """
        logger.debug(f"Searching for item with name '{item_name}'")
        try:
            # Wait for elements to appear and return handles
            locator = page.get_by_text(item_name)
            locator.wait_for(state="attached", timeout=timeout)  # Wait for at least one element to attach
            elements = locator.element_handles()  # Get all element handles
            logger.debug(f"Found {len(elements)} elements matching query '{item_name}'.")
            return elements
        except PlaywrightTimeoutError:
            logger.error(f"No elements matching query '{item_name}' found within {timeout / 1000} seconds.")
            return []

