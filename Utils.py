from random import random

def navigateToCategory(page,category):
    page.goto("https://demoqa.com")
    page.locator("xpath=.//h5[contains(text(), 'Elements')]").click()
    page.locator(f"xpath=.//ul//li//span[contains(text(), '{category}')]").click()
    return page

def generateFieldValue(field_name, field_type:str, field_length:int):
    data = {}
    if field_type == "text":
        data[field_name] = f"{field_name}{round(100*random())}"
    elif field_type == "email":
        data[field_name] = f"{field_name}{round(100*random())}@email.com"
    elif field_type == "date":
        data[field_name] = f"20{round(30*random())}.{round(12*random())}.{round(28*random())}"
    elif field_type == "phone":
        data[field_name] = f"{round((10**field_length-1)*random())}"
    return data


class Utils:
    def __init__(self,page,data = None):
        self.page = page
        self.data = data
        self.form = page.locator("xpath=.//form")

    def fillInputorTextarea(self,text,xpath,parent=None):
        input_locator = parent.locator(f"xpath={xpath}") if parent is not None else self.page.locator(f"xpath={xpath}")
        input_locator.fill(text)

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
            # print(f"Utils ind {ind}: {wrapper_locator.text_content()}")
            input_locator.fill(data_values[ind]) #

    def clickRadioButton(self, xpath, parent=None):
        button_locator = parent.locator(f"xpath={xpath}//input") if parent is not None else self.page.locator(
            f"xpath={xpath}//input")
        try:
            button_locator.click(force=True)
            return 1
        except Exception as e:
            print(f"Error: Cannot click button:{button_locator}", e)
        return 0

    def clickButton(self,xpath,parent=None,clicktype=""):
        button_locator = parent.locator(f"xpath={xpath}") if parent is not None else self.page.locator(f"xpath={xpath}")
        if clicktype == "":
            button_locator.click(force=True)
        elif clicktype == "dbl":
            button_locator.dblclick(force=True)
        elif clicktype == "right":
            button_locator.click(force=True, button="right")


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