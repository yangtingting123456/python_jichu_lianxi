import os,xlrd
import StudentBaseInfo
from utils.config_utils import conf
class ReadExcel:
    def __init__(self,excel_path,sheet_name):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
    # 读取excel中的数据制作成列表，对象的封装
    def read_excel_list(self):
        WorkBook = xlrd.open_workbook(self.excel_path)
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
        WorkBook = xlrd.open_workbook(self.excel_path)
        sheet = WorkBook.sheet_by_name(self.sheet_name)
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
    excel_path = os.path.join(current_path, conf.get_excel_path())
    RD_excel = ReadExcel(excel_path,'StudentInfo')
    print(RD_excel.read_excel_list())
    for i in range(len(RD_excel.read_excel_obj())):
        print(RD_excel.read_excel_obj()[i].name)