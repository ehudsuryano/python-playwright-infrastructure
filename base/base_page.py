from playwright.sync_api import Page


class BasePage:
    """
    Base class for all page objects. Contains shared methods and utilities.
    """

    def __init__(self, page: Page):
        self.page = page

    def load(self):
        """
        Navigates the browser to the given URL.
        This method should be overridden in child classes.
        """
        raise NotImplementedError("The 'load' method must be overridden in the child class.")

    def get_title(self):
        """
        Returns the title of the current page.
        """
        return self.page.title()

    def get_url(self):
        """
        Returns the current URL of the browser.
        """
        return self.page.url

    def scroll_to_element(self, element_text: str):
        """
        Scrolls the page to the first element containing the specified text.

        :param element_text: Text of the element to scroll to
        """
        element = self.page.locator(f"//*[text()='{element_text}']").first
        element.scroll_into_view_if_needed()
        return element

    def is_element_exist(self, selector: str):
        """
        Checks if an element exists on the page.

        :param selector: CSS or XPath selector for the element
        :return: True if the element exists, False otherwise
        """
        return self.page.locator(selector).count() > 0
