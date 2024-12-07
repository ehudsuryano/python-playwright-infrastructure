from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from utilities.logger import get_logger

logger = get_logger()


class BaseHandler:
    def __init__(self, driver):
        self.driver = driver
