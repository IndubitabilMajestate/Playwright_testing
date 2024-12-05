from Playwright.Utils import Utils

class Form:
    def __init__(self,page,data = None):
        self.page = page
        self.data = data
        self.form = None

    def fillForm(self,xpath=None,data=None):
        if data is None:
            data = self.data
        form_locator = self.page.locator(f"xpath={xpath}//form")
        form_field_wrappers = form_locator.locator("xpath=.//div[contains(translate(@id,'W','w'),'wrapper')]")
        for form_field_wrapper in form_field_wrappers.all():
            # print('----------------------------------------------------------------')
            labels_count = form_field_wrapper.locator("xpath=.//label").count()
            wrapper_label = form_field_wrapper.locator("xpath=.//label").text_content() if (
                    labels_count == 1) else 'Gender' if labels_count == 3 else 'Hobbies'
            # print(wrapper_label)
            # print(form_field_wrapper.locator("xpath=//input").count())
            if wrapper_label not in self.data.keys():
                continue
            input_locators = form_field_wrapper.locator("xpath=.//input | .//textarea | .//select | .//button")
            if input_locators.count() > 1:
                for input_locator in input_locators.all():
                    input_type = input_locator.get_attribute("type")
                    tag_type = input_locator.evaluate("el => el.tagName.toLowerCase()")
                    if (input_type == 'text' or tag_type == "textarea") and 'react-select' not in input_locator.get_attribute('id'):
                        key_name = input_locator.get_attribute('placeholder') if input_locator.get_attribute('placeholder') else (
                            input_locator.get_attribute('value'))
                        self.fillInputorTextarea(data[wrapper_label][key_name], "", input_locator)
                    elif input_type == 'radio' or input_type == 'checkbox':
                        key_name = input_locator.get_attribute('value')
                        # print(wrapper_label!='Gender' and key_name in self.data[wrapper_label], self.data[wrapper_label])
                        if (wrapper_label == 'Gender' and key_name == self.data['Gender']) or key_name in self.data[wrapper_label]:
                            button_locator = Utils(input_locator)
                            # print(button_locator)
                            button_locator.clickButton(".")
                    elif 'react-select' in input_locator.get_attribute('id'):
                        index = 0 if '3' in input_locator.get_attribute('id') else 1
                        self.fillInputorTextarea(self.data[wrapper_label][index] ,"",input_locator,True)
                    else:
                        pass
            else:
                if form_field_wrapper.locator("xpath=//input").count() > 0:
                    input_locator = form_field_wrapper.locator("xpath=.//input")
                    if isinstance(self.data[wrapper_label],list):
                        for data in self.data[wrapper_label]:
                            self.fillInputorTextarea(data, "", input_locator,True)
                    else:
                        self.fillInputorTextarea(self.data[wrapper_label], "", input_locator, wrapper_label=='Date of Birth')
                elif form_field_wrapper.locator("xpath=//textarea").count() > 0:
                    input_locator = form_field_wrapper.locator("xpath=.//textarea")
                    self.fillInputorTextarea(self.data[wrapper_label], "", input_locator)
                elif form_field_wrapper.locator("xpath=//select").count() > 0:
                    pass
                elif form_field_wrapper.locator("xpath=//button").count() > 0:
                    pass

    def fillInputorTextarea(self,text,xpath,parent=None,enter=False):
        input_locator = parent.locator(f"xpath={xpath}//.") if parent is not None else self.page.locator(f"xpath={xpath}//.")
        input_locator.fill(text)
        if enter:
            # print('Pressed Enter')
            input_locator.press('Enter')

    def getOutputData(self,xpath="", parent=None):
        output_locator = parent.locator(f"xpath={xpath}//div[@id='output']") if parent is not None else self.page.locator(f"xpath={xpath}//div[@id='output']")
        data = {}
        if output_locator.locator("xpath=.//p").count() > 0:
            for output_data in output_locator.locator("xpath=.//p").all():
                data[output_data.text_content().split(':')[0].strip()] = output_data.text_content().split(':')[1].strip()
        return data