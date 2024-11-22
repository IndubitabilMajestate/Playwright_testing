class Form:
    def __init__(self,page,data = None):
        self.page = page
        self.data = data
        self.form = None

    def fillForm(self,xpath=None,data=None):
        if data is None:
            data = {}
        form_locator = self.page.locator(f"xpath={xpath}//form")
        form_field_wrappers = form_locator.locator("xpath=.//div[(.//input or .//textarea or .//select or .//button) and .//label]")
        for form_field_wrapper in form_field_wrappers.all():
            wrapper_label = form_field_wrapper.locator("xpath=.//label").text_content()
            # print(wrapper_label)
            # print(form_field_wrapper.locator("xpath=//input").count())
            if form_field_wrapper.locator("xpath=//input").count() > 0:
                input_locator = form_field_wrapper.locator("xpath=//input")
                self.fillInputorTextarea(data[wrapper_label], "", input_locator)
            elif form_field_wrapper.locator("xpath=//textarea").count() > 0:
                input_locator = form_field_wrapper.locator("xpath=.//")
                self.fillInputorTextarea(data[wrapper_label], "", input_locator)
            elif form_field_wrapper.locator("xpath=//select").count() > 0:
                pass
            elif form_field_wrapper.locator("xpath=//button").count() > 0:
                pass

    def fillInputorTextarea(self,text,xpath,parent=None):
        if parent is not None:
            parent.fill(text)
        else:
            try:
                self.page.locator(f"xpath={xpath}").fill(text)
            except:
                print("No valid input or textarea!")