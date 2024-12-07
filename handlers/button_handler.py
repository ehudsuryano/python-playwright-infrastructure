from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from utilities.logger import get_logger
from base.base_handler import BaseHandler
logger = get_logger()


class ButtonHandler(BaseHandler):
    @staticmethod
    def on_get_elements(page: Page, btn: str, timeout: int = 10000):
        """
        Wait for and return all web elements matching the query.

        :param page: Playwright's Page instance
        :param btn: String to locate elements (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the elements (default is 10,000 ms)
        :return: List of element handles found using the constructed XPath, or an empty list if none are found
        """
        xpath = (f"//button[@type='button' and @id='submit']|" +
                 f"//button[@type='submit' and @role='button' and @value='{btn}']|" +
                 f"//button[@type='submit' and @role='button' and @value='{btn}']|" +
                 f"//button[@id='submit']"
                 )

        logger.debug(f"Constructed XPath: {xpath}")
        try:
            # Wait for elements to appear and return handles
            locator = page.locator(xpath)
            locator.wait_for(state="attached", timeout=timeout)  # Wait for at least one element to attach
            elements = locator.element_handles()  # Get all element handles
            logger.debug(f"Found {len(elements)} elements matching query '{btn}'.")
            return elements
        except PlaywrightTimeoutError:
            logger.error(f"No elements matching query '{btn}' found within {timeout / 1000} seconds.")
            return []
