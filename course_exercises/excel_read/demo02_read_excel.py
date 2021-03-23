import os
import xlrd
#读取excel中的数据制作成列表，对象
#1.读取数据保存为列表
#[[学号，姓名，年龄，性别，成绩],[学号，姓名，年龄，性别，成绩],[]]
#创建工作簿对象
current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, 'data/StudentInfo.xlsx')
WorkBook = xlrd.open_workbook(excel_path)
# #获取工作簿的第一张表
sheet01 = WorkBook.sheet_by_name('StudentInfo')
all_student_info = []
n = sheet01.nrows
l = sheet01.ncols
for i in range(1,sheet01.nrows):  #总行
    row_student_info = []
    for j in range(sheet01.ncols):  #总列
        row_student_info.append(sheet01.cell_value(i,j))
    all_student_info.append(row_student_info)
print(all_student_info)
for i in all_student_info:
    print(i)


#2.读取数据保存为对象
#[对象1：['学号','姓名','年龄','乘积']]
import StudentBaseInfo
current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, 'data/StudentInfo.xlsx')
WorkBook = xlrd.open_workbook(excel_path)
#获取工作簿的第一张表
sheet = WorkBook.sheet_by_name('StudentInfo')
all_student_obj=[]
#-----方法1：获取每个单元格然后赋值
#-----方法2：循环获取保存
for i in range(1,sheet.nrows):
    students = StudentBaseInfo.StudentBaseInf(sheet.cell_value(i,0),
                               sheet.cell_value(i,1),
                               sheet.cell_value(i,2),
                               sheet.cell_value(i,3),
                               sheet.cell_value(i,4))
    all_student_obj.append(students)

for i in range(len(all_student_obj)):
    print(all_student_obj[i].name)




