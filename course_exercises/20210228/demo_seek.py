import os
#修改文件的读写位置，产生位移
current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path,'demo02.txt')
file_txt = open(file_path,'rb')  #使用二进制模式不需要添加额外的编码
print(file_txt.read(3))
print(file_txt.tell()) #获取当前文件的位置
#0表示从文件的开头，1表示从文件的当前位置，2表示文件末尾
#在文件中没有使用二进制模式（b）打开文件，那么只允许从文件的起始位置即使算相对位置产生位移。
file_txt.seek(-1,2)  #产生位移
print(file_txt.read(3))
file_txt.close()