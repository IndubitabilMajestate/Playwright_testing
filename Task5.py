from random import random
from Locator import Locator
from playwright.sync_api import sync_playwright

def Task5():
    with sync_playwright() as playwright:
        chromium = playwright.chromium  # or "firefox" or "webkit".
        browser = chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demoqa.com")
        page.locator("xpath=.//h5[contains(text(), 'Elements')]").click()
        page.locator("xpath=.//ul//li//span[contains(text(), 'Check Box')]").click()

        locator = Locator(page)

        # Expand and Collapse test
        locator.clickButton(".//button[contains(@title,'Expand')]")
        if page.locator('xpath=.//ol').count() > 1:
            print("Expand test passed!")
        locator.clickButton(".//button[contains(@title,'Collapse')]")
        if page.locator('xpath=.//ol').count() == 1:
            print("Collapse test passed!")

        # Checkbox test
        locator.clickButton(".//button[contains(@title,'Expand')]")
        locator.clickButton(".//label[.//span[text()='Documents']]//input")
        #if locator.


if __name__ == '__main__':
    Task5()