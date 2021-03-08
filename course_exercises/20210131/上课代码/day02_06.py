'''
@File : day02_06.py
@Time : 2021/1/31 15:43
@Author: luoman
'''
# import lib
# for 遍历 ---字符串，列表，字典
'''
for 变量 in 字符串/列表：
    执行语句
'''
str1 = 'hello'
print(str1)
print(str1[2:5])

for i in str1:
    print(i)

for i in range(0, len(str1)):
    print(str1[i])

list01 = ['张三', '李四', '王五']
for j in list01:
    print(j)
# 要求出输出列表的元素
print(list(enumerate(list01, start=100)))

# 遍历字典
# 方法一：字典的函数get()--通过键获取值
dict01= {'x':1, 'y':2, 'z':3}
for key in dict01:
    print(key, dict01.get(key))

for key in dict01:
    print(key)
# 方法二：输出key和value
for key, value in dict01.items():
    print(key, value)






