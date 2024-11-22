from random import random
from Utils import Utils, navigateToCategory
from playwright.sync_api import sync_playwright

def Task4():
    with sync_playwright() as playwright:
        page = playwright.chromium.launch(headless=False).new_page()
        page = navigateToCategory(page,'Web Tables')

        locator = Utils(page)
        # Read webtable test
        table = locator.readTableData(".//div[@class='web-tables-wrapper']")
        print(table)

        # Add data test
        first_name = f"Name{round(100 * random())}"
        last_name = f"Last_Name{round(100 * random())}"
        data = {"First Name": first_name,
                "Last Name": last_name,
                "Email": f"{first_name+last_name}@example.com",
                "Age": f"{round(100*random())}",
                "Salary":f"{round(10000 * random())}",
                "Department":f"Department{round(10 * random())}"}
        locator.clickButton("//button[text()='Add']")
        locator.fillForm("",data)
        locator.clickButton("//button[text()='Submit']")
        # Search first
        table = locator.readTableData(".//div[@class='web-tables-wrapper']")
        if data in table.values():
            print(f"Data entered successfully!\n{data}")
        pass
        # Search data test
        locator.fillInputorTextarea(f'{data["First Name"]}',".//input[@id='searchBox']")
        table = locator.readTableData(".//div[@class='web-tables-wrapper']")
        if data in table.values():
                print(f"Data found in table!\n{data}")
        pass
        # Modify data test
        locator.fillInputorTextarea('',".//input[@id='searchBox']")
        table = locator.readTableData(".//div[@class='web-tables-wrapper']")
        modify_index = [key for key,val in table.items() if val == data][0]
        if modify_index:
            print(f"Data found in table!\n{modify_index}:{table[modify_index]}")
        locator.clickButton(f"//span[contains(@id,'edit-record-{modify_index + 1}')]")
        new_data = data
        new_data["Salary"] = "10000"; new_data["Department"] = 'Department20'
        locator.fillForm("",new_data)
        locator.clickButton("//button[text()='Submit']")
        table = locator.readTableData(".//div[@class='web-tables-wrapper']")
        if new_data in table.values():
                print(f"Data modified successfully!\n{new_data}")
        pass
        # Delete data test
        locator.fillInputorTextarea(f'', ".//input[@id='searchBox']")
        table = locator.readTableData(".//div[@class='web-tables-wrapper']")
        del_index = [key for key, val in table.items() if val == new_data][0]
        if del_index:
            print(f"Data found in table!\n{del_index}:{table[del_index]}")
        locator.clickButton(f"//span[contains(@id,'delete-record-{del_index + 1}')]")
        table = locator.readTableData(".//div[@class='web-tables-wrapper']")
        if data not in table.values():
            print(f"Data not found in table!")
        pass



if __name__ == '__main__':
    Task4()