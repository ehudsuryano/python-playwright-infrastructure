from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from utilities.logger import get_logger
from base.base_handler import BaseHandler

logger = get_logger()


class TextboxHandler(BaseHandler):
    @staticmethod
    def on_get_elements(page: Page, query: str, timeout: int = 10000):
        """
        Wait for and return all web elements matching the query.

        :param page: Playwright's Page instance
        :param query: String to locate elements (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the elements (default is 10,000 ms)
        :return: List of element handles found using the constructed XPath, or an empty list if none are found
        """
        xpath = (
            f"//textarea[@name='{query}' or @title='{query}' or @id='{query}']|"
            f"//input[@name='{query}' and (@type='text' or @type='password')]|"
            f"//input[@title='{query}' and (@type='text' or @type='password')]|"
            f"//input[@id='{query}' and (@type='text' or @type='password' or @type='email')]"
        )

        logger.debug(f"Constructed XPath: {xpath}")

        try:
            # Wait for elements to appear and return handles
            locator = page.locator(xpath)
            locator.wait_for(state="attached", timeout=timeout)  # Wait for at least one element to attach
            elements = locator.element_handles()  # Get all element handles
            logger.debug(f"Found {len(elements)} elements matching query '{query}'.")
            return elements
        except PlaywrightTimeoutError:
            logger.error(f"No elements matching query '{query}' found within {timeout / 1000} seconds.")
            return []
