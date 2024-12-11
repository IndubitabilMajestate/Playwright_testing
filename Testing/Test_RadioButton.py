import pytest

from Playwright.Utils import Utils


@pytest.mark.parametrize("page_setup",[('Elements',"Radio Button")],indirect=True)
class Test_RadioButton:
    cases = [
        [],
        ['Yes'],
        ['Impressive'],
        ['No'],
        ['Yes','Impressive','No']
    ]

    @pytest.fixture(scope='function', params=cases)
    def data_setup(self, request):
        data = request.param
        yield data


    def test_RadioButton(self,page_setup, data_setup):
        root_locator = Utils(page_setup)

        output_text = ""
        if not data_setup:
            assert root_locator.page.locator('xpath=.//p//span').count() == 0
            root_locator.page.reload()
            return
        for button_name in data_setup:
            root_locator.clickButton(f'.//div[contains(label,"{button_name}")]//input')
            if button_name != 'No':
                output_text = root_locator.page.locator('xpath=.//p//span').text_content()
                assert output_text == button_name
            else:
                try:
                    assert output_text == root_locator.page.locator('xpath=.//p//span').text_content()
                except:
                    assert True

        root_locator.page.reload()

