import pytest

from Playwright.Utils import Utils


@pytest.mark.parametrize('page_setup',['Buttons'],indirect=True)
class Test_Buttons:
    cases = [
        [],
        ['Double '],
        ['Right '],
        [''],
        ['Double ','Right ','']
    ]

    @pytest.fixture(scope='function', params=cases)
    def data_setup(self, request):
        data = request.param
        yield data

    def test_Buttons(self,page_setup, data_setup):
        root_locator = Utils(page_setup)
        buttons_list = data_setup
        if not buttons_list:
            assert root_locator.page.locator('xpath=.//p').count() == 0
            root_locator.page.reload()
            return
        for button in buttons_list:
            output_text = ""
            if button == 'Double ':
                click_type = 'dbl'
                output_text = "double"
            elif button == 'Right ':
                click_type = 'right'
                output_text = "right"
            else:
                click_type = ""
                output_text = "dynamic"
            root_locator.clickButton(f'.//button[text()="{button}Click Me"]',click_type=click_type)
            assert root_locator.page.locator(f'xpath=.//p[contains(text(),{output_text})]').count() == 1
        root_locator.page.reload()


