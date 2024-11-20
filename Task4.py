from random import random

from Locator import Locator
from playwright.sync_api import sync_playwright

def Task4():
    with sync_playwright() as playwright:
        chromium = playwright.chromium  # or "firefox" or "webkit".
        browser = chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demoqa.com")
        page.locator("xpath=.//h5[contains(text(), 'Elements')]").click()
        page.locator("xpath=.//ul//li//span[contains(text(), 'Web Tables')]").click()


        locator = Locator(page)
        # Double-Click button test
        table = locator.readTableData(".//div[@class='web-tables-wrapper']")
        # print(table)

        first_name = f"Name{round(100 * random())}"
        last_name = f"Last_Name{round(100 * random())}"
        email = f"{first_name+last_name}@example.com"
        age = f"{round(100*random())}"
        salary = f"{round(10000 * random())}"
        department = f"Department{round(10 * random())}"
        data = {"First Name": first_name, "Last Name": last_name, "Email": email, "Age": age, "Salary":salary, "Department":department}
        locator.clickButton("//button[text()='Add']")
        locator.fillForm("",data)
        locator.clickButton("//button[text()='Submit']")


if __name__ == '__main__':
    Task4()