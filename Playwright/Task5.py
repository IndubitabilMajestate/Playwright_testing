from random import random
from Utils import Utils, navigateToCategory
from playwright.sync_api import sync_playwright

def Task5():
    with sync_playwright() as playwright:
        page = navigateToCategory(playwright.chromium.launch(headless=False).new_page(),'Elements','Check Box')
        locator = Utils(page)

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