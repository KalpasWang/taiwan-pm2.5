import os, ast, requests, json
from openpyxl import load_workbook

url = 'http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json'
html = requests.get(url).text#.encode('utf-8-sig')

json_data = ast.literal_eval(html)
# print(json.dumps(json_data[0], indent=2))

wb_name = 'pm25.xlsx'
wb = load_workbook(wb_name)
print(wb)
