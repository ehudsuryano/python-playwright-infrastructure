from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError
from utilities.logger import get_logger
from base.base_handler import BaseHandler

logger = get_logger()


class TextboxHandler(BaseHandler):
    @staticmethod
    def on_get_elements(page: Page, query: str, timeout: int = 10000):
        """
        Wait for and return all web elements matching the query using Playwright's modern locator methods.
        Optimized for performance while maintaining reliability.

        :param page: Playwright's Page instance
        :param query: String to locate elements (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the elements (default is 10,000 ms)
        :return: List of element handles found using various locator strategies
        """
        logger.debug(f"Searching for elements with query: {query}")

        try:
            # Combine most common selectors into a single locator for better performance
            main_locator = page.locator(f"""
                input[name='{query}'][type='text'],
                input[name='{query}'][type='password'],
                input[name='{query}'][type='email'],
                input[title='{query}'],
                textarea[name='{query}'],
                textarea[title='{query}'],
                #{query},
                [placeholder='{query}']
            """)

            # Try the combined selector first with the full timeout
            try:
                main_locator.wait_for(state="attached", timeout=timeout)
                elements = main_locator.element_handles()
                if elements:
                    logger.debug(f"Found {len(elements)} elements with main locator.")
                    return elements
            except PlaywrightTimeoutError:
                pass

            # If main locator fails, try these additional locators with a shorter timeout
            additional_locators = [
                page.get_by_role("textbox", name=query),
                page.get_by_label(query),
                page.get_by_test_id(query)
            ]

            elements = []
            seen_elements = set()
            short_timeout = timeout // 3  # Shorter timeout for additional locators

            for locator in additional_locators:
                try:
                    locator.wait_for(state="attached", timeout=short_timeout)
                    for handle in locator.element_handles():
                        try:
                            element_id = f"{handle.get_attribute('id')}:{handle.get_attribute('name')}:{handle.get_attribute('type')}"
                            if element_id not in seen_elements:
                                seen_elements.add(element_id)
                                elements.append(handle)
                        except Exception:
                            elements.append(handle)
                except PlaywrightTimeoutError:
                    continue

            logger.debug(f"Found {len(elements)} total unique elements matching query '{query}'.")
            return elements

        except PlaywrightTimeoutError as e:
            logger.error(f"Error while searching for elements with query '{query}': {str(e)}")
            return []