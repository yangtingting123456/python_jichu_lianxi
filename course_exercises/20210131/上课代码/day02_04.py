'''
@File : day02_04.py
@Time : 2021/1/31 14:12
@Author: luoman
'''
# import lib
# 循环：
'''
当代码中有重复操作语句的时候
语法形式：
while 表达式:
   [缩进]语句块
[else:
   [缩进]语句块]
'''
# 举例：要求一行输出5个*符号
# print('*', end='\t')
# print('*', end='\t')
# print('*', end='\t')
# print('*', end='\t')
# print('*', end='\t')
count = 1   # 起始条件
while count <= 5:  # 结束的判断条件
    print('*', end='\t')  # 循环体
    count = count + 1  # 步长
else:
    print('\n打印结束！！')
# 注意事项：1、循环一定是有重复的操作
#         2、循环要有四个条件才能进行：a、要有起始值   b、要知道什么结束  c、要有循环执行语句--循环体  d、步长
# 算出1--100的和
# + 法运算符---二元运算符 a+b  1+2=值 值+3 。。。。值+100
sum = 0

# sum = sum + 1
# sum = sum + 2
# sum = sum + 3
# sum = sum + 4
# sum = sum + 5
# sum = sum + 6
# sum = sum + 7
# sum = sum + 8
# sum = sum + 9
# sum = sum + 10
# ..
# sum = sum +100
i = 1
while i <= 100:
    sum = sum + i
    i = i+1
else:
    print(sum)
# 循环是可以发生嵌套的：
'''
while 表达式：
   while 表达式：
       [缩进]循环体
   else：
       执行语句
else:
   执行语句
'''
# 要求输出5行，每一行是5个*号
# count = 1   # 起始条件
# while count <= 5:  # 结束的判断条件
#     print('*', end='\t')  # 循环体
#     count = count + 1  # 步长
# else:
#     print('\n')
#
# count = 1   # 起始条件
# while count <= 5:  # 结束的判断条件
#     print('*', end='\t')  # 循环体
#     count = count + 1  # 步长
# else:
#     print('\n')
#
# count = 1   # 起始条件
# while count <= 5:  # 结束的判断条件
#     print('*', end='\t')  # 循环体
#     count = count + 1  # 步长
# else:
#     print('\n')
#
# count = 1   # 起始条件
# while count <= 5:  # 结束的判断条件
#     print('*', end='\t')  # 循环体
#     count = count + 1  # 步长
# else:
#     print('\n')
#
# count = 1   # 起始条件
# while count <= 5:  # 结束的判断条件
#     print('*', end='\t')  # 循环体
#     count = count + 1  # 步长
# else:
#     print('\n')

row = 1
while row <= 5:
    count = 1  # 起始条件
    while count <= 5:  # 结束的判断条件
        print('*', end='\t')  # 循环体
        count = count + 1  # 步长
    else:
        print('\n')

    row = row + 1

# 循环也可以跟if语句嵌套
















