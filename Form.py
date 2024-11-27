class Form:
    def __init__(self,page,data = None):
        self.page = page
        self.data = data
        self.form = None

    def fillForm(self,xpath=None,data=None):
        if data is None:
            data = {}
        form_locator = self.page.locator(f"xpath={xpath}//form")
        form_field_wrappers = form_locator.locator("xpath=.//div[contains(translate(@id,'W','w'),'wrapper')]")
        for form_field_wrapper in form_field_wrappers.all():
            wrapper_label = form_field_wrapper.locator("xpath=.//label").text_content()
            # print(wrapper_label)
            # print(form_field_wrapper.locator("xpath=//input").count())
            input_locators = form_field_wrapper.locator("xpath=.//input | .//textarea | .//select | .//button")
            if input_locators.count() > 1:
                for input_locator in input_locators.all():
                    input_type = input_locator.get_attribute("type")
                    tag_type = input_locator.get_attribute("tagName").lower()
                    if input_type == 'text' or tag_type == "textarea":
                        key_name = input_locator.get_attribute('placeholder') if input_locator.get_attribute('placeholder') else (
                            input_locator.get_attribute('value'))
                        self.fillInputorTextarea(data[wrapper_label][key_name], "", input_locator)
                    elif form_field_wrapper.locator("xpath=//textarea").count() > 0:
                        input_locator = form_field_wrapper.locator("xpath=.//")
                        self.fillInputorTextarea(data[wrapper_label], "", input_locator)
                    elif form_field_wrapper.locator("xpath=//select").count() > 0:
                        pass
                    elif form_field_wrapper.locator("xpath=//button").count() > 0:
                        pass
            else:
                if form_field_wrapper.locator("xpath=//input").count() > 0:
                    input_locator = form_field_wrapper.locator("xpath=.//input")
                    self.fillInputorTextarea(data[wrapper_label], "", input_locator)
                elif form_field_wrapper.locator("xpath=//textarea").count() > 0:
                    input_locator = form_field_wrapper.locator("xpath=.//")
                    self.fillInputorTextarea(data[wrapper_label], "", input_locator)
                elif form_field_wrapper.locator("xpath=//select").count() > 0:
                    pass
                elif form_field_wrapper.locator("xpath=//button").count() > 0:
                    pass

    def fillInputorTextarea(self,text,xpath,parent=None):
        input_locator = parent.locator(f"xpath={xpath}//.") if parent is not None else self.page.locator(f"xpath={xpath}//.")
        input_locator.fill(text)