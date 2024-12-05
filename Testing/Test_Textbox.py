from random import random

import pytest
from playwright.sync_api import sync_playwright
from Playwright.Utils import navigateToCategory
from Playwright.Form import Form


class Test_Textbox:
    cases = [
        {},
        {'Full Name':f'Name{round(10*random())}'},
        {'Full Name': f'Name{round(10 * random())}', 'Email': f'email{round(10 * random())}@test.com'},
        {'Full Name': f'Name{round(10 * random())}', 'Email': f'email{round(10 * random())}@test.com', 'Current Address': f'Street{round(10 * random())}', 'Permanent Address': f'Street{round(10 * random())}'}
    ]
    @pytest.fixture(scope='class')
    def page_setup(self, request):
        with sync_playwright() as playwright:
            page = navigateToCategory(playwright.chromium.launch(headless=False).new_page(), 'Elements', 'Text Box')
            yield page

    @pytest.fixture(scope='function',params=cases)
    def data_setup(self,request, page_setup):
        data = request.param
        yield data

    def test_Textbox(self,page_setup, data_setup):
        page = page_setup
        data = data_setup
        form = Form(page,data)
        form.fillForm('.')
        page.locator('xpath=.//button[contains(text(),"Submit")]').click()
        output_data = form.getOutputData(xpath=".")
        # print(output_data)
        if 'Permananet Address' in output_data.keys():
            output_data['Permanent Address'] = output_data.pop('Permananet Address')
        if 'Name' in output_data.keys():
            output_data['Full Name'] = output_data.pop('Name')
        assert output_data == data
