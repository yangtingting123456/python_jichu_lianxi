# Python考试试卷
# 一、选择题（2分一题）
# 1、python不支持的数据类型有  
# A、char  B、int  C、float  D、list
# 2、如下代码，结果是
# x = “foo”  y = 2  
# print(x+y) 
# A.foo        B.foofoo  C.foo2   D.报错
# 3、以下不能创建列表的是
# A、dic1 = {}    B、dic2 = {123:345}   C、dic3 = {[1,2,3]:'uestc'}   D、dic3 = {(1,2,3):'uestc'}
# 4、以下代码输出结果是：
# Kvps = {‘1’:1,’2’:2}
# theCopy = kvps
# kvps[‘1’] = 5
# sum = kvps[‘1’] + theCopy[‘1’] 
# Print(sum)
# A.1      B.2              C.7     D.10
# 5、以下何者是不合法的布尔表达式：
# A.x in range(6)     B.3=a   C.e>5 and 4==f  D.(x-6)>5
# 6、下列表达式的值为True的是
# A.5+4j>2-3j    B.3>2==2    C.e>5 and 4==f  D.(x-6)>5
# 7、已知x=43,ch=‘A’,y = 1,则表达式(x>=y and ch<‘b’ and y)的值是
# A、0   B、1  C、出错  D、True
# 8、下列Python语句正确的事
# A、min = x if x < y else y    B、max = x >y ? x : y  C、if(x>y) print(x)   D、while True pass
# 9、下述while循环执行的次数为
# k=1000
# while k>1:
#    print k
#    k=k/2
# A.9   B.10    C.11  D.100
# 10、Python如何定义一个函数
# A、class<name>(<type> arg1,<type> arg2,…<type>argN)
# B、function <name>(arg1,arg2,…argN)
# C、def <name>(arg1,arg2,…argN)
# D、def <name>(<type> arg1,<type> arg2,…<type>argN)
# 二、填空题：（1空1分）
# 1、python中的函数有四种参数类型 _________、________、__________、________
# 2、有字符串”12345678”, 切片操作后的值是：[2:0] _______   [2:-1]_________
# 3、面向对象编程的三大特性是什么_______  _______  ________
# 4、python构造函数的名称是_________
# 5、导入模块的关键是_____________
# 6、构造初始化的时候，self表示_________
# 7、获取list的元素个数是用 _______函数,往list里面添加元素用_______函数
# 8、使用python获取当前时间戳的写法是 _____
# 9、文件打开的函数是_________,打开文件的模式有________________
# 10、python重命名文件的写法________、删除文件的写法_______、判断目录是否存在的写法________
# 三、问答题
# 1、如何使用python获取当前的时间，要求年月日时分秒都显示
# 2、可变长度参数 *a 和 **b 有什么区别？
# 3、Python字典有哪几种操作方法（至少写4种），并说明其含义
# 4、Range函数用在什么场合？如果range(-1,3) 能表示的数字是哪些？
# 5、List和tuple在python中有哪些区别？
# 6、继承实现的作用是什么？

# 四、编程题目：
# 1、请写一段代码，把list列表[2,5,1,6,8,9]中从大到小进行排列
def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n  - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [2,5,1,6,8,9]
bubbleSort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i]),


# 2、用循环的方式实现 20以内的奇数相加

total = 0
for i in range(0,21):
    if i % 2 ==1:
        total = i+total
print('20以内的奇数相加:',total)


# 3、有一个列表[5,3,7,5,20],请用冒泡算法对其进行排序
def bubbleSort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [5,3,7,5,20]
bubbleSort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i]),
# 4、循环创建100个文件，文件的名字任意，内容都是hello
import os
import random
file_name = random.randint(1,12321)
a = open('a.txt','w+')
a.write('hello')
