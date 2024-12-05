from Utils import Utils,navigateToCategory
from playwright.sync_api import sync_playwright

def Task3():
    with sync_playwright() as playwright:
        page = navigateToCategory(playwright.chromium.launch(headless=False).new_page(),'Elements','Buttons')

        locator = Utils(page)
        # Double-Click button test
        locator.clickButton("//button[text()='Double Click Me']/parent::div//button", click_type='dbl')
        if page.locator("xpath=//p[contains(text(),'double')]").text_content() == "You have done a double click":
            print("Test passed!")
        pass
        # Right-Click button test
        locator.clickButton("//button[text()='Right Click Me']/parent::div//button", click_type='right')
        if page.locator("xpath=//p[contains(text(),'right')]").text_content() == "You have done a right click":
            print("Test passed!")
        pass
        # Dynamic-Click button test
        locator.clickButton("//button[text()='Click Me']/parent::div//button")
        if page.locator("xpath=//p[contains(text(),'dynamic')]").text_content() == "You have done a dynamic click":
            print("Test passed!")
        pass

if __name__ == '__main__':
    Task3()