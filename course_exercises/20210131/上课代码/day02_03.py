'''
@File : day02_03.py
@Time : 2021/1/31 11:22
@Author: luoman
'''
# import lib
'''
python程序控制语句
1、程序的运行顺序有三种：
   按从上往下的顺序执行
   按选择的顺序执行
   按重复的顺序执行
'''
'''
选择结构语句：出现了代码分支
基本形式为：
if 判断条件：
    [缩进]执行语句块…… 
else：
    [缩进]执行语句块……

'''
if False:
    print('条件成立')
else:
    print('条件不成立')

# 举例：比较两个数的大小
# 输入两个数，比较两个数的大小，输出最大的数
a = int(input('数字1:'))
b = int(input('数字2：'))

if a > b:
    print('恭喜您，找到最大值啦！！')
    print('最大值为:', a)
else:
    print('恭喜您，找到最大值啦！！')
    print('最大值为:', b)

'''
if 表达式：
  [缩进]执行语句块……
elif 表达式:
  [缩进]执行语句块……
elif 表达式:
  [缩进]执行语句块……
else:
  [缩进]执行语句块……
'''
# 举例：根据工资的多少选择旅游的地点：
# 假设工资50000---欧洲游  20000--50000：日韩游  10000-20000：国内游  5000--10000：省内游
# 2000--5000:市内游  2000以下：梦游
sal = int(input('输入你的工资来选择旅游去向吧：'))
if sal >= 50000:
    print('欧洲游')
elif sal >= 20000 and sal < 50000:
    print('日韩游')
elif sal >= 10000 and sal< 20000:
    print('国内游')
elif sal >= 5000 and sal< 10000:
    print('省内游')
elif sal >= 2000 and sal <5000:
    print('市内游')
elif sal>=0 and sal <2000:
    print('梦游')
else:
    print('输入的工资有误')

# if 语句的嵌套
# 举例：比较两个数的大小，输出最大值，如果两数相等，则提示两个是相等的
i = int(input('输入第一个数：'))
j = int(input('输入第二个数：'))
if i==j:
    print('两个数是相等的')
else:
    if i>j:
        print('最大的是:', i)
    else:
        print('最大的是:', j)
# python 是没有 switch语句；







