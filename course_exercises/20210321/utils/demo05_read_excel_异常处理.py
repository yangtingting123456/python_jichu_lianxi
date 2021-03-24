#异常处理
#1.让try的范围更广
#2.根据实际需求，让代码自动自动回复一个默认值
import os,xlrd
import StudentBaseInfo
from config_utils import config
from log_utils import log_obj
class ReadExcel:
    def __init__(self,excel_path,sheet_name):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
    # 读取excel中的数据制作成列表，对象的封装
    def read_excel_list(self):
        log_obj.info('将excel中的数据封装成列表')
        try:
            WorkBook = xlrd.open_workbook(self.excel_path)
            log_obj.info('创建工作簿成功')
        except FileNotFoundError as  e:
            log_obj.error('文件路径不存在，系统自动给默认路径')
            current_path = os.path.dirname(__file__)
            excel_path1 = os.path.join(current_path, '../data/StudentInfo.xlsx')
            log_obj.info('获取系统默认路径%s'%excel_path1)
            WorkBook = xlrd.open_workbook(excel_path1)
            log_obj.info('创建工作簿成功')
        sheet = WorkBook.sheet_by_name(self.sheet_name)
        all_student_info = []
        for i in range(1, sheet.nrows):  # 总行
            row_student_info = []
            for j in range(sheet.ncols):  # 总列
                row_student_info.append(sheet.cell_value(i, j))
            all_student_info.append(row_student_info)
        return all_student_info
    # 2.对象的封装
    def read_excel_obj(self):
        log_obj.info('将excel里面的数据封装成对象')
        try:
            WorkBook = xlrd.open_workbook(self.excel_path)
            log_obj.info('创建工作簿成功')
        except FileNotFoundError as  e:
            log_obj.error('文件路径不存在，系统自动给默认路径')
            current_path = os.path.dirname(__file__)
            excel_path1 = os.path.join(current_path, '../data/StudentInfo.xlsx')
            log_obj.info('使用系统默认路径%s'%excel_path1)
            WorkBook = xlrd.open_workbook(excel_path1)
            log_obj.info('创建工作簿成功')
        sheet = WorkBook.sheet_by_name(self.sheet_name)
        log_obj.info('获取某一张工作簿')
        all_student_obj = []
        for i in range(1, sheet.nrows):
            students = StudentBaseInfo.StudentBaseInf(sheet.cell_value(i, 0),
                                                      sheet.cell_value(i, 1),
                                                      sheet.cell_value(i, 2),
                                                      sheet.cell_value(i, 3),
                                                      sheet.cell_value(i, 4))
            all_student_obj.append(students)
        return all_student_obj
#测试类
if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, config.get_excel_path())
    RD_excel = ReadExcel(excel_path,'StudentInfo')
    print(RD_excel.read_excel_list())
    for i in range(len(RD_excel.read_excel_obj())):
        print(RD_excel.read_excel_obj()[i].name)