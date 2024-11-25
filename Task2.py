from Utils import Utils,navigateToCategory
from playwright.sync_api import sync_playwright

def Task2():
    with sync_playwright() as playwright:
        page = navigateToCategory(playwright.chromium.launch(headless=False).new_page(),'Elements','Radio Button')

        locator = Utils(page)
        # Test Yes Button
        if locator.clickRadioButton(".//div[./label[text()='Yes']]") and page.locator("xpath=.//p//span").text_content() == 'Yes':
            print("Test passed!")

        # Test Impressive Button
        if locator.clickRadioButton(".//div[./label[text()='Impressive']]") and page.locator("xpath=.//p//span").text_content() == 'Impressive':
            print("Test passed!")
        pass
        # Test No Button
        if not locator.clickRadioButton(".//div[./label[text()='No']]") and page.locator("xpath=.//p//span").text_content() != 'No':
            print("Test passed!")


if __name__ == '__main__':
    Task2()