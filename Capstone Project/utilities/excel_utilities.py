import openpyxl
import os


def get_login_data(file_name):

    project_root = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(project_root, "test_data", file_name)

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password, browser, first_name, last_name, address, province, postal_code = row
        data.append(
            (username, password, browser, first_name, last_name, address, province, postal_code)
        )

    return data