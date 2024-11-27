from random import random
from playwright.sync_api import sync_playwright
from Utils import navigateToCategory
from Form import Form

def Task6():
    with sync_playwright() as playwright:
        page = navigateToCategory(playwright.chromium.launch(headless=False).new_page(),'Forms','Practice Form')
        data = {
            'Name' : {'First Name': f'FirstName{round(10*random())}', 'Last Name': f'LastName{round(10*random())}'},
            'Email' : f'email{round(10*random())}@test.com',
            'Gender' : 'Male' if round(3*random()) == 0 else 'Female' if round(3*random()) == 1 else 'Other',
            'Mobile' : f'{round(9999999999*random())}',
            'Date of Birth': f'{round(28*random())}.{round(12*random())}.19{50+round(49*random())}',
            'Subjects' : 'English\nMaths\n', ## not ok
            'Hobbies': [1, 3],
            'Current Address': f'Street no.{round(100*random())}'
        }

        form_locator = Form(page,data)
        form_locator.fillForm("",data)

if __name__ == '__main__':
    Task6()