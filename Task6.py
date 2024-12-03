from random import random
from playwright.sync_api import sync_playwright
from Utils import navigateToCategory, Utils
from Form import Form
from WebTable import Webtable


def Task6():
    with sync_playwright() as playwright:
        page = navigateToCategory(playwright.firefox.launch(headless=False).new_page(),'Forms','Practice Form')
        page.add_style_tag(content="""
            iframe, [id*='ads'], [class*='ads'], .banner {
                display: none !important;
            }
        """)
        data = {
            'Name' : {'First Name': f'FirstName{round(10*random())}', 'Last Name': f'LastName{round(10*random())}'},
            'Email' : f'email{round(10*random())}@test.com',
            'Gender' : 'Male' if round(3*random()) == 0 else 'Female' if round(3*random()) == 1 else 'Other',
            'Mobile(10 Digits)' : f'{round(9999999999*random())}',
            'Date of Birth': f'{round(12*random())}.{round(28*random())}.19{50+round(49*random())}',
            'Subjects' : ['English', 'Maths', 'Chemistry'], ## not ok
            'Hobbies': ['1', '3'],
            'Current Address': f'Street no.{round(100*random())}',
            'State and City': ['NCR', 'Delhi']
        }

        form_locator = Form(page,data)
        form_locator.fillForm("",data)
        submit_button_locator = Utils(Utils(page).form.locator('xpath=.//button[@id="submit"]'))
        submit_button_locator.clickButton('.')
        submit_button_locator.page.press('Enter')
        table = Webtable(page)
        table_data = table.readTableData('.//div[contains(@class,"table")]')
        print(table_data)

if __name__ == '__main__':
    Task6()