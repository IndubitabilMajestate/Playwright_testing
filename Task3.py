from Locator import Locator
from playwright.sync_api import sync_playwright

def Task3():
    with sync_playwright() as playwright:
        chromium = playwright.chromium  # or "firefox" or "webkit".
        browser = chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demoqa.com")
        page.locator("xpath=.//h5[contains(text(), 'Elements')]").click()
        page.locator("xpath=.//ul//li//span[contains(text(), 'Buttons')]").click()


        locator = Locator(page)
        # Double-Click button test
        if locator.doubleClickButton("//button[text()='Double Click Me']/parent::div") and locator.getPText("//p[contains(text(),'double')]") == "You have done a double click":
            print("Test passed!")
        pass
        if locator.rightClickButton("//button[text()='Right Click Me']/parent::div") and locator.getPText(
                "//p[contains(text(),'right')]") == "You have done a right click":
            print("Test passed!")
        pass
        if locator.clickButton("//button[text()='Click Me']/parent::div") and locator.getPText(
                "//p[contains(text(),'dynamic')]") == "You have done a dynamic click":
            print("Test passed!")
        pass

if __name__ == '__main__':
    Task3()