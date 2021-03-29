#写文件
import os
current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path,'demo01.txt')
file_txt = open(file_path,'a+',encoding='utf-8')  #r+也会覆盖之前的内容,a+和r+没有什么区别
file_txt.write('Are you OK? \n Hi,hello world')
file_txt.flush()  #只要文件的内容有改变，就需要flush
file_open_txt = open(file_path,'r+',encoding='utf-8')
print(file_open_txt.readlines())
file_txt.close()

current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path,'demo01.txt')
