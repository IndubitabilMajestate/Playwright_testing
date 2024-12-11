from random import random

import pytest

from Playwright.Form import Form
from Playwright.Utils import Utils
from Playwright.WebTable import Webtable


@pytest.mark.parametrize('page_setup',[('Elements','Web Tables')],indirect=True)
class Test_WebTable:

    @pytest.fixture(scope='class')
    def data_setup(self):
        data = {
            'First Name': f'FirstName{round(10 * random())}',
            'Last Name': f'LastName{round(10 * random())}',
            'Email': f'email{round(10 * random())}@test.com',
            'Age': f'{20 + round(40 * random())}',
            'Salary': f'{3000 + round(2000 * random())}',
            'Department': f'Department{round(10 * random())}'
        }
        yield data

    def test_CreateEntry(self,page_setup, data_setup):
        root_locator = Utils(page_setup)
        root_locator.clickButton('.//button[text()="Add"]')
        # Generate new_entry for the new entry
        new_entry = data_setup
        # Get the form, fill and submit it
        form = Form(root_locator.page, data=new_entry)
        form.fillForm(xpath='.', data=new_entry)
        root_locator.clickButton('.//button[text()="Submit"]')
        # Search for the created entry
        root_locator.fillInputorTextarea(new_entry['First Name'], './/input[@id="searchBox"]')
        # Get the webtable and its contents
        webtable = Webtable(root_locator.page)
        table_data = webtable.readTableData(".//div[@class='web-tables-wrapper']")

        assert table_data[0] == new_entry

    def test_ModifyEntry(self,page_setup, data_setup):
        root_locator = Utils(page_setup)
        # Search for the specified entry
        specified_entry = data_setup
        root_locator.fillInputorTextarea(specified_entry['First Name'], './/input[@id="searchBox"]')
        # New entry data
        specified_entry['Salary'] = '100'
        root_locator.clickButton("//span[contains(@id,'edit-record')]")
        # Get the form, fill and submit it
        form = Form(root_locator.page, data=specified_entry)
        form.fillForm(xpath='.', data=specified_entry)
        root_locator.clickButton('.//button[text()="Submit"]')
        # Search for the created entry
        root_locator.fillInputorTextarea(specified_entry['First Name'], './/input[@id="searchBox"]')
        # Get the webtable and its contents
        webtable = Webtable(root_locator.page)
        table_data = webtable.readTableData(".//div[@class='web-tables-wrapper']")
        assert table_data[0] == specified_entry

    def test_DeleteEntry(self,page_setup,data_setup):
        root_locator = Utils(page_setup)
        # Search for the specified entry
        specified_entry = data_setup
        root_locator.fillInputorTextarea(specified_entry['First Name'], './/input[@id="searchBox"]')
        # Delete the specified entry
        root_locator.clickButton("//span[contains(@id,'delete-record')]")
        # Search for the specified entry
        root_locator.fillInputorTextarea(specified_entry['First Name'], './/input[@id="searchBox"]')
        # Get the webtable and its contents
        webtable = Webtable(root_locator.page)
        table_data = webtable.readTableData(".//div[@class='web-tables-wrapper']")
        assert table_data == {}
