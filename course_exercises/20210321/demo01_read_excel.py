import xlrd
import os
#excel操作
#使用xlrd模块，第三方工具包，可以读取xlsx,xls的excel文件(版本必须使用1.2.0)，xlwt 写入数据到excel中
#创建工作簿对象
current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, 'data/StudentInfo.xlsx')
WorkBook = xlrd.open_workbook(excel_path)
#获取工作簿的第一张表
sheet01 = WorkBook.sheet_by_name('StudentInfo')
#获取工作簿的数据,获取列,获取行
print('获取sheet的总列数：',sheet01.ncols)
print('获取sheet的总行数：',sheet01.nrows)
print('获取某一个表格的数据：',sheet01.cell_value(0,1))
#获取第一行数据或第一列数据
print('获取第一行数据：',sheet01.row(1))
print('获取第一列数据：',sheet01.col(1))
#类型,1.   0  empty         2.   1    string    3.   2   number     4.    3 date
#    5.    4    boolean    6.   5     error
print('单元格类型：',sheet01.cell_type(1,1))


