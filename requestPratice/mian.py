import requests

from api.api_key import ApiKey
from case.test_excel_read import ExcelRead
# #
# url = "http://39.98.138.157:5000/api/login"
# data = {
#     "username": "admin",
#     "password": "123456"
# }
# response = requests.post(url=url, json=data)
# # print(response.text)
# dic_json = response.json()
# print(type(dic_json))
# ak = ApiKey()
# print(ak.get_text(dic_json, "$..msg"))
#
#
# print(a)


e = ExcelRead("case/api_cases.xlsx")
sheet_list = e.get_sheet_name()
for sheet in sheet_list:
    print(sheet)
    # e.get_sheet_by_sheet_name(sheet)
    e.send_requests(sheet)
    break
