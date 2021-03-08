'''
@File : day02_05.py
@Time : 2021/1/31 14:58
@Author: luoman
'''
# import lib

# for 两个作用
# 1、仅仅是循环
# 2、进行对象的遍历
'''
range()函数的作用是：生成数字序列
range()函数有三个参数：1-起始值  2-结束值  3-步长
range()函数是 包头不包尾的
for 变量 in range()
    [缩进]循环体
'''
# 打印一行5个*号
for star in range(1, 6, 1):
    print('*', end='\t')
else:
    print('\n')
# range() 只写一个参数---表示结束值，默认从0开始，步长为1

for star in range(6):
    print('*', end='\t')
else:
    print('\n')

# range() 可以写两个参数---表示开始值，结束值，默认步长为1

for star in range(1, 6):
    print('*', end='\t')
else:
    print('\n')

# for 循环也可以嵌套
for i in range(1, 6, 1): # 行数
    for star in range(1, 6):
        print('*', end='\t')
    else:
        print('\n')

# 九九乘法表
for i in range(1, 10, 1): # 行数
    for j in range(1, i+1, 1): # 个数
        print('%d*%d=%d'%(j, i, i*j), end='\t')
    else:
        print('\n')
list01 = list( x for x in range(1, 10))
print(list01)

list02 = list( x for x in range(1, 10) if x >=5)
print(list02)

age = [20, 30, 40, 50, 60]
list03 = list(x for x in age if x >=40)
print(list03)


