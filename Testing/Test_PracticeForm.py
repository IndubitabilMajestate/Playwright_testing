from datetime import datetime
from random import random

import pytest

from Playwright.Form import Form
from Playwright.Utils import Utils
from Playwright.WebTable import Webtable


def formatData(original_data):
    modified_data = {}
    for key, entry in original_data.items():
        if entry['Values'] == '':
            continue
        else:
            if entry['Label'] == 'Student Name':
                modified_data['Name'] = {'First Name':entry['Values'].split(' ')[0],'Last Name':entry['Values'].split(' ')[1]}
            elif entry['Label'] == 'Student Email':
                modified_data['Email'] = entry['Values']
            elif entry['Label'] == 'Mobile':
                modified_data['Mobile(10 Digits)'] = entry['Values']
            elif entry['Label'] == 'Date of Birth':
                normalized_date = datetime.strptime(entry['Values'], '%d %B,%Y')
                if normalized_date.date() == datetime.today().date():
                    continue
                modified_data[entry['Label']] = f'{normalized_date.month}.{normalized_date.day}.{normalized_date.year}'
            elif entry['Label'] == 'Subjects':
                modified_data[entry['Label']] = entry['Values'].split(', ')
            elif entry['Label'] == 'Hobbies':
                hobbies_list = entry['Values'].split(', ')
                modified_data[entry['Label']] = []
                if 'Sports' in hobbies_list:
                    modified_data[entry['Label']].append('1')
                if 'Reading' in hobbies_list:
                    modified_data[entry['Label']].append('2')
                if 'Music' in hobbies_list:
                    modified_data[entry['Label']].append('3')
            elif entry['Label'] == 'Address':
                modified_data['Current Address'] = entry['Values']
            elif entry['Label'] == 'State and City':
                modified_data[entry['Label']] = entry['Values'].split(' ')
            else:
                modified_data[entry['Label']] = entry['Values']
    return modified_data


@pytest.mark.parametrize('page_setup',[('Forms','Practice Form')],indirect=True)
class Test_PracticeForm():

    def test_FullEntry(self,page_setup):
        root_locator = Utils(page_setup)
        # Data to be entered
        data = {
            'Name': {'First Name': f'FirstName{round(10 * random())}', 'Last Name': f'LastName{round(10 * random())}'},
            'Email': f'email{round(10 * random())}@test.com',
            'Gender': 'Male' if round(3 * random()) == 0 else 'Female' if round(3 * random()) == 1 else 'Other',
            'Mobile(10 Digits)': f'{round(9999999999 * random())}',
            'Date of Birth': f'{round(12 * random())}.{round(28 * random())}.19{50 + round(49 * random())}',
            'Subjects': ['English', 'Maths', 'Chemistry'],  ## not ok
            'Hobbies': ['1', '3'],
            'Current Address': f'Street no.{round(100 * random())}',
            'State and City': ['NCR', 'Delhi']
        }
        form = Form(root_locator.page, data)
        form.fillForm("", data)
        submit_button_locator = Utils(Utils(root_locator.page).form.locator('xpath=.//button[@id="submit"]'))
        submit_button_locator.clickButton('.')
        submit_button_locator.page.press('Enter')
        table = Webtable(root_locator.page)
        table_data = table.readTableData('.//div[contains(@class,"table")]')
        root_locator.page.locator('xpath=.//button[text()="Close"]').click()
        assert data == formatData(table_data)


    @pytest.mark.xfail
    def test_MissingEntry(self, page_setup):
        root_locator = Utils(page_setup)
        # Data to be entered
        data = {
            'Email': f'email{round(10 * random())}@test.com',
            'Gender': 'Male' if round(3 * random()) == 0 else 'Female' if round(3 * random()) == 1 else 'Other',
            'Mobile(10 Digits)': f'{round(9999999999 * random())}',
            'Date of Birth': f'{round(12 * random())}.{round(28 * random())}.19{50 + round(49 * random())}',
            'Subjects': ['English', 'Maths', 'Chemistry'],  ## not ok
            'Hobbies': ['1', '3'],
            'Current Address': f'Street no.{round(100 * random())}',
            'State and City': ['NCR', 'Delhi']
        }
        form = Form(root_locator.page, data)
        form.fillForm("", data)
        submit_button_locator = Utils(Utils(root_locator.page).form.locator('xpath=.//button[@id="submit"]'))
        submit_button_locator.clickButton('.')
        submit_button_locator.page.press('Enter')
        table = Webtable(root_locator.page)
        table_data = table.readTableData('.//div[contains(@class,"table")]')
        root_locator.page.locator('xpath=.//button[text()="Close"]').click()

        assert data == formatData(table_data)


    def test_MandatoryOnly(self,page_setup):
        root_locator = Utils(page_setup)
        # Data to be entered
        data = {
            'Name': {'First Name': f'FirstName{round(10 * random())}', 'Last Name': f'LastName{round(10 * random())}'},
            'Email': f'email{round(10 * random())}@test.com',
            'Gender': 'Male' if round(3 * random()) == 0 else 'Female' if round(3 * random()) == 1 else 'Other',
            'Mobile(10 Digits)': f'{round(9999999999 * random())}',
            'Date of Birth': f'{round(12 * random())}.{round(28 * random())}.19{50 + round(49 * random())}',
            'Current Address': f'Street no.{round(100 * random())}',
        }
        form = Form(root_locator.page, data)
        form.fillForm("", data)
        submit_button_locator = Utils(Utils(root_locator.page).form.locator('xpath=.//button[@id="submit"]'))
        submit_button_locator.clickButton('.')
        submit_button_locator.page.press('Enter')
        table = Webtable(root_locator.page)
        table_data = table.readTableData('.//div[contains(@class,"table")]')
        root_locator.page.locator('xpath=.//button[text()="Close"]').click()

        assert data == formatData(table_data)
