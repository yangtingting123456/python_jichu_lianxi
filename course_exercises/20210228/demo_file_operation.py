import os
current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path,'demo02.txt')
#文件常用操作
# 1.文件重命名
# os.rename(file_path,current_path+'\demo02.py')   #文件重命名
# os.remove(current_path+'/p7.txt')  #删除文件
# os.mkdir('p7.txt')  #新建目录
# os.rmdir(current_path+'/p7.txt')  #删除空目录
# os.makedirs(current_path+'/a/b/c')  #传经多次目录
# os.rmdir(current_path+'/a')
# print(os.getcwd())  #获取当前工作目录
# os.chdir(current_path+'/a')  #改变当前系统工作路径
# print(os.getcwd())  #获取当前工作目录
#判断文件是否存在
print(os.path.isfile(file_path))   #判断文件是否存在
print(os.path.isdir(current_path+'/a'))  #判断目录是否存在




