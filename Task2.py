from Locator import Locator
from playwright.sync_api import sync_playwright

def Task2():
    with sync_playwright() as playwright:
        chromium = playwright.chromium  # or "firefox" or "webkit".
        browser = chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demoqa.com")
        page.locator("xpath=.//h5[contains(text(), 'Elements')]").click()
        page.locator("xpath=.//ul//li//span[contains(text(), 'Radio Button')]").click()


        locator = Locator(page)
        # Test Yes Button
        if locator.clickRadioButton(".//div[label[text()='Yes']]") and locator.getSpanValue(".//p") == 'Yes':
            print("Test passed!")

        # Test Impressive Button
        if locator.clickRadioButton(".//div[label[text()='Impressive']]") and locator.getSpanValue(".//p") == 'Impressive':
            print("Test passed!")

        # Test No Button
        if locator.clickRadioButton(".//div[label[text()='No']]") and locator.getSpanValue(".//p") != 'No':
            print("Test passed!")


if __name__ == '__main__':
    Task2()