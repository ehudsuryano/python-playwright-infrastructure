from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from utilities.logger import get_logger
from base.base_handler import BaseHandler
logger = get_logger()


class CardHandler(BaseHandler):
    @staticmethod
    def on_get_elements(page: Page, card_name: str, timeout: int = 10000):
        """
        Wait for and return all web elements matching the query.

        :param page: Playwright's Page instance
        :param card_name: String to locate elements (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the elements (default is 10,000 ms)
        :return: List of element handles found , or an empty list if none are found
        """

        logger.debug(f"Searching for card with name '{card_name}'")

        try:
            # Wait for elements to appear and return handles
            locator = page.get_by_text(card_name)
            locator.wait_for(state="visible", timeout=timeout)  # Wait for at least one element to attach
            elements = locator.element_handles()  # Get all element handles
            logger.debug(f"Found {len(elements)} elements matching query '{card_name}'.")
            return elements
        except PlaywrightTimeoutError:
            logger.error(f"No elements matching query '{card_name}' found within {timeout / 1000} seconds.")
            return []
