import allure
import os
from playwright.sync_api import Page


def capture_screenshot(page: Page, name: str):
    """
    Captures a screenshot of the current browser state and attaches it to the Allure report.

    Args:
        page (Page): The Playwright Page instance.
        name (str): Name for the screenshot file (without extension).
    """
    # Define the reports folder path one level above the current directory
    reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "reports"))
    os.makedirs(reports_dir, exist_ok=True)  # Ensure the directory exists

    # Set the full path for the screenshot
    screenshot_path = os.path.join(reports_dir, f"{name}.png")

    # Save the screenshot locally
    page.screenshot(path=screenshot_path)

    # Attach the screenshot to the Allure report
    with open(screenshot_path, "rb") as image_file:
        allure.attach(
            image_file.read(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
