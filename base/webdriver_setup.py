from playwright.sync_api import sync_playwright


class WebDriverSetup:
    @staticmethod
    def get_browser(browser="chrome", headless=False):
        """
        Initialize and return a Playwright browser instance.

        :param browser: Name of the browser ("chrome", "firefox", "edge", or "safari").
        :param headless: Whether to run the browser in headless mode (default: False).
        :return: Playwright browser instance.
        """
        browser = browser.lower()
        playwright = sync_playwright().start()

        if browser == "chrome" or browser == "chromium":
            browser_instance = playwright.chromium.launch(headless=headless)
        elif browser == "firefox":
            browser_instance = playwright.firefox.launch(headless=headless)
        elif browser == "edge":
            browser_instance = playwright.chromium.launch(channel="msedge", headless=headless)
        elif browser == "safari":
            raise ValueError("Safari is not supported by Playwright on non-WebKit systems. Use 'webkit' instead.")
        elif browser == "webkit":
            browser_instance = playwright.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Browser '{browser}' is not supported.")

        return browser_instance

    @staticmethod
    def get_context(browser_instance, options=None):
        """
        Create and return a browser context.

        :param browser_instance: Playwright browser instance.
        :param options: Dictionary of browser context options.
        :return: Playwright browser context instance.
        """
        options = options or {}
        context = browser_instance.new_context(**options)
        return context
