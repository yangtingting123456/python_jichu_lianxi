'''
@File : day02_1.py
@Time : 2021/1/31 09:11
@Author: luoman
'''
# import lib
# 输入--input---通过键盘输入的都是字符串
i = input("请输入一个字母:")  # 按回车键表示结束输入
# 输出 print() # print() 默认结束时，带有换行符
print(i)
print("结果为:", i)
j = int(input('输入一个整数'))
print("J的结果为:", j, i)
print("我今年", j, "岁了")# 不推荐输出的
print("我今年%d岁了" % j, end='\t')  # \t表示制表符---tab
print("我想出去玩")
# str.format() 输出
# 例：我的名字是张三，我今年20岁了
name = "张三"
age = 20
print('我的名字是%s，我今年%d岁了' % (name, age))

print('我的名字是{}，我今年{}岁了'.format(name, age))

print('我的名字是{n}，我今年{a}岁了'.format(n="罗曼", a=20))
print('我的名字是{n}，我今年{a}岁了'.format(n=name, a=age))
print('我的名字是{0}，我今年{1}岁了'.format(name, age))





