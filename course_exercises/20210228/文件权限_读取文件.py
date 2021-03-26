#文件操作：IO流
#语法：  文件对象名称 = Open(‘文件路径’，‘权限’，缓冲)
import os
current_path = os.path.dirname(__file__)
file_py = os.path.join(current_path,'demo01.txt')
#写入内容到文件
# demo01 = open(file_py,'w+')
# demo01.write('this is demo01 file ')
# demo01.flush()
# print(demo01.mode)
# print(demo01.encoding)
# print(demo01.name)
# demo01.close()    #如果文件流不关闭没有什么事情，也有可能会导致内存溢出。
# print(demo01.closed)

#读取文件内容
#1.read 无参数的时候，默认全部读完，结果是当作一个字符串
# r_file = open(file_py,'r+',encoding='utf-8')
# r_content = r_file.read()
# print(r_content)
# r_file.close()

#2.read 有参数时  一个字母占1个字节，一个汉字占两个字节
# r_file = open(file_py,'r+',encoding='utf-8')
# r_content02 = r_file.read(4)
# print(r_content02)
# r_cont03 = r_file.read(3)
# print(r_cont03)   #会从上一次读取的地方接着读取
# r_file.close()

#3.按行读取
r_file = open(file_py,'r+',encoding='utf-8')
r_content04 = r_file.readline(50)   #readline无参数读取一行，有参数表示读取的字符数，有参数，最多也读取一行
r_content05 = r_file.readlines()  #readlines 方法没有参数就是默认读取所有行，结果会保存在list中，
print(r_content05,type(r_content05))                                   # 有参数不足一行或者超过一行一行则会显示下一行的内容
print(r_content04,type(r_content04))
r_file.close()
