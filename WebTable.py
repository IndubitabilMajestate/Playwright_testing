class Webtable:
    def __init__(self, root):
        self.root = root

    def readTableData(self, xpath=None):
        table_locator = self.root.locator(f"xpath={xpath}")
        # print(table_locator)
        header_row = table_locator.locator("xpath=.//div[@class='rt-thead -header']//div[@role='row'] | .//thead//tr")
        # print(header_row.count())
        headers = {}
        if header_row.count() > 0:
            index = 0
            header_columns = header_row.locator("xpath=.//div[@role='columnheader'] | .//th")
            # print(header_columns.count())
            for col in header_columns.all():
                headers[index] = col.text_content()
                index+=1
        # print(headers)
        rows_locator = table_locator.locator("xpath=.//div[@class='rt-tbody']//div[@role='rowgroup'] | .//tbody//tr")
        # print(rows_locator.count())
        table_data = {}
        for row_index, row in enumerate(rows_locator.all()):
            row_data = {}
            cells = row.locator("xpath=.//div[@role='gridcell'] | .//td")
            # print(cells.count())
            for cell_index, cell in enumerate(cells.all()):
                cell_value = cell.text_content()
                if cell_value == "\xa0" or cell_value == " ":
                    if cell_index == 0: return  table_data
                    else: break
                # print(cell_value)
                if headers:
                    column_name = headers[cell_index]
                    row_data[column_name] = cell_value
                else:
                    row_data[cell_index] = cell_value
            table_data[row_index] = row_data
        return table_data