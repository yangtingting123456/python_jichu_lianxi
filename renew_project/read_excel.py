import xlrd
import os
current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'date/login_data.xlsx')
#创建一个工作簿
wokebook = xlrd.open_workbook(excel_path)
#获取第一个sheet
sheet = wokebook.sheet_by_name('login_data')
#获取sheet的总行数
rows = sheet.nrows
#获取sheet的总列数
cols = sheet.ncols
