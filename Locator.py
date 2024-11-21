class Locator:
    def __init__(self,page,data = None):
        self.page = page
        self.data = data
        self.form = page.locator("xpath=.//form")

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


    def checkNodeChildren(self,parent=None):
        pass

    def fillInputorTextarea(self,text,xpath,parent=None):
        if parent is not None:
            parent.fill(text)
        else:
            try:
                self.page.locator(f"xpath={xpath}").fill(text)
            except:
                print("No valid input or textarea!")

    def fillInputLocator(self):
        wrapper_locator_list = self.form.locator("xpath=.//div[contains(@id,'wrapper')]")
        num_fields = wrapper_locator_list.count()
        data_keys = list(self.data.keys())
        data_values = list(self.data.values())
        for ind in range(num_fields): #for wrapper_locator in wrapper_locator_list.all():
            wrapper_locator = wrapper_locator_list.nth(ind)
            input_locator = wrapper_locator.locator(f"xpath="
                f"//label[text()='{data_keys[ind]}']/parent::div/following-sibling::div//input | "
                f"//label[text()='{data_keys[ind]}']/parent::div/following-sibling::div//textarea | "
                f"//label[text()='{data_keys[ind]}']/parent::div/following-sibling::div//button | "
                f"//label[text()='{data_keys[ind]}']/parent::div/following-sibling::div//select")
            # label -> tip de input -> actiune specifica
            # attributes = input_locator.evaluate("""
            #             (el) => {
            #                 const attrs = {};
            #                 for (let i = 0; i < el.attributes.length; i++) {
            #                     const attr = el.attributes[i];
            #                     attrs[attr.name] = attr.value;
            #                 }
            #                 return attrs;
            #             }
            #         """)
            #print(attributes)
            # print(f"Locator ind {ind}: {wrapper_locator.text_content()}")
            input_locator.fill(data_values[ind]) #

    def clickRadioButton(self, xpath, parent=None):
        if parent:
            button_locator = parent.locator(f"xpath={xpath}//input")
        else:
            button_locator = self.page.locator(f"xpath={xpath}//input")
        try:
            button_locator.click(force=True)
            return 1
        except Exception as e:
            print(f"Error: Cannot click button:", e)
        return 0

    def doubleClickButton(self,xpath,parent=None):
        if parent:
            button_locator = parent.locator(f"xpath={xpath}//button")
        else:
            button_locator = self.page.locator(f"xpath={xpath}//button")
        button_locator.dblclick()

    def rightClickButton(self,xpath,parent=None):
        if parent:
            button_locator = parent.locator(f"xpath={xpath}//button")
        else:
            button_locator = self.page.locator(f"xpath={xpath}//button")
        button_locator.click(button='right')

    def getPText(self, xpath, parent=None):
        if parent is not None:
            p_locator = parent.locator(f"xpath={xpath}//p")
        else:
            p_locator = self.page.locator(f"xpath={xpath}//p")
        return p_locator.text_content()

    def getSpanValue(self, xpath, parent=None):
        if parent is not None:
            span_locator = parent.locator(f"xpath={xpath}//span")
        else:
            span_locator = self.page.locator(f"xpath={xpath}//span")
        return span_locator.text_content()

    def readTableData(self, xpath=None):
        table_locator = self.page.locator(f"xpath={xpath}")
        # print(table_locator)
        header_row = table_locator.locator("xpath=.//div[@class='rt-thead -header']//div[@role='row']")
        # print(header_row.count())
        headers = {}
        if header_row.count() > 0:
            index = 0
            header_columns = header_row.locator("xpath=.//div[@role='columnheader']")
            # print(header_columns.count())
            for col in header_columns.all():
                headers[index] = col.text_content()
                index+=1
        # print(headers)
        rows_locator = table_locator.locator("xpath=.//div[@class='rt-tbody']//div[@role='rowgroup']")
        # print(rows_locator.count())
        table_data = {}
        row_index = 0
        for row in rows_locator.all():
            row_data = {}
            cells = row.locator("xpath=.//div[@role='gridcell']")
            # print(cells.count())
            cell_index = 0
            for cell in cells.all():
                if cell_index == 6:
                    break
                cell_value = cell.text_content()
                if cell_index==0 and cell_value == "\xa0":
                    return table_data
                # print(cell_value)
                if headers:
                    column_name = headers[cell_index]
                    row_data[column_name] = cell_value
                else:
                    row_data[cell_index] = cell_value
                cell_index +=1
            table_data[row_index] = row_data
            row_index+=1
        return table_data

    def clickButton(self,xpath,parent=None):
        if parent:
           button_locator = parent.locator(f"xpath={xpath}")
        else:
            button_locator = self.page.locator(f"xpath={xpath}")
        button_locator.click()

    def validateRadioButtonFunctionality(self,xpath):
        radio_button_list = self.page.locator(xpath)
        number_of_buttons = radio_button_list.count()
        print(number_of_buttons)
        for ind in range(number_of_buttons):  # ca mai sus
            button = radio_button_list.nth(ind)
            button_name = button.locator("xpath=.//label").text_content()
            #trebuie sa verific daca e enabled
            self.clickButton(f"xpath=.//input", button)
            # verific span cu ce valoare are in el

    def validateResponse(self):
        output_locator_list = self.form.locator("xpath=.//div[@id='output']//p")
        data_keys = list(self.data.keys())
        data_values = list(self.data.values())
        validation = len(data_keys)
        for ind in range(len(data_keys)):
            output_field = output_locator_list.nth(ind)
            [field_name, field_value] = output_field.text_content().replace(" :",":").split(":")
            if field_name == "Permananet Address": field_name = "Permanent Address" # Existe liniile
            if field_value == data_values[ind] and field_name in data_keys[ind]:
                validation-=1
            else:
                print(f"Expected {data_keys[ind]}:{data_values[ind]}; got {field_name}:{field_value}!")
                return False
        if validation == 0:
            return True