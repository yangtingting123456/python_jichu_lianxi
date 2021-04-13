# 1、根据用户输入的玫瑰花的朵数输出其代表的意义：在古代希腊神话中，玫瑰花集爱情与美丽于一身，所以人们常用玫瑰来表达爱情，但是不同的朵数带表的含义是不同的。
#    1朵表是：你是我的唯一。3朵表是：我爱你。10朵表示：十全十美。99朵表示：天长地久。108朵表示：求婚！
print('       1朵表是：你是我的唯一。       ')
print('       3朵表是：我爱你。            ')
print('       10朵表示：十全十美。         ')
print('       99朵表示：天长地久。         ')
print('       108朵表示：求婚！         ')
print("-----------------------------------")
flower = int(input('请输入你要购买的花朵数：'))
if flower ==1:
    print("你是我的唯一")
elif flower == 3:
    print("我爱你")
elif flower == 10:
    print("十全十美")
elif flower == 99:
    print("天长地久")
elif flower == 108:
    print("求婚")
else:
    print("你输入的数字不存在")

# 2、国家对酒驾的规定是：车辆驾驶人员血液中的酒精含量小于20mg/100ml不构成饮酒驾驶行为。含量大于或者等于20mg/100ml,
# 小于80mg/100ml为饮酒驾车，酒精含量大于或者等于80mg/100ml加醉驾车。现写一段代码判断输入的血液酒精含量是否为酒驾。
volume = int(input('请输入您测试的酒精量，单位mg:'))
if volume < 20 and volume >= 0:
    print('不构成饮酒驾驶')
elif volume >= 20 and volume < 80:
    print("饮酒驾车")
elif volume >= 80:
    print("加醉驾车")
else:
    print("输入有误")

# 3、小明身高1.75m，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = float(input("请输入你的身高，单位m："))
weight = float(input("请输入你的体重，单位kg："))
bmi = int((weight/(height*height)))
print("您的bmi指数是:%d"%bmi)
if bmi<18.5 and bmi>=0:
    print("你的身体状况是过轻")
elif bmi>=18.5 and bmi<25:
    print("你的身体状况正常")
elif bmi>=25 and bmi<28:
    print("你的身体状况过重")
elif bmi>=28 and bmi < 32:
    print("你的身体状况肥胖")
elif bmi>=32:
    print("你的身体状况严重肥胖")
else:
    print("亲，您的输入有误，请重新输入！")

# 4、使用循环语句计算从1到100，一共有多少个尾数为7或者7的倍数这样的数，请输出这样的数。
for i in range(1,101):
    if i%10/7==1 or i%7==0:
        print('1到100内尾数为7或7的倍数有：%i：'%i)

# 5、模拟支付宝的蚂蚁森林通过日常的走步--20g，生活缴费--50g，线下支付--100g，网络购票--80g，共享单车--200g等低碳，环保行为可以积攒能量，
# 当能量达到一定数量后，可以种一棵真正的树--500g。由用户输入环保行为，来积累能量；查询能量请输入能量来源！退出程序请输入0。
print("---------- 0.推出程序。 ----------")
print("---------- 1.日常的走步--20g。 ----------")
print("---------- 2.生活缴费--50g。 ----------")
print("---------- 3.线下支付--100g。 ----------")
print("---------- 4.网络购票--80g 。 ----------")
print("---------- 5.共享单车--200g。 ----------")
print("--------------------------------------")
count_emergy = 0
while(count_emergy>=0):
    emergy = int(input("你输入你的环保行为："))
    if emergy == 1:
        count_emergy = count_emergy + 20
    elif emergy == 2:
        count_emergy += 50
    elif emergy == 3:
        count_emergy += 100
    elif emergy == 4:
        count_emergy += 80
    elif emergy == 5:
        count_emergy += 200
    elif emergy==0:
        break;

if count_emergy >=500:
   print("恭喜你，你成功种了一棵树")
print(count_emergy)

# 6、猜数字游戏，随机生成一个1到10之间的数(包括1和10)的数字作为基准数，玩家每次通过键盘输入一个数字，
# 如果输入的数字和基准数字相同，则过关，否则重新输入。如果玩家输入-1，则表示退出游戏。
import random
range_num = random.randint(1,10)
print('随机数字是：%d'%range_num)
while (range_num>0 and range_num<11):
    input_num = int(input("请输入1到10的数字："))
    if input_num == range_num:
       print("----  过关 -----")
       pass
    elif input_num == -1:
        break;

# 7、编写程序，设置您的余额，流量和剩余通话时间。模拟10086自助查询系统的功能：
# 输入1，显示您当前的余额；输入2，显示您当前剩余的流量，单位为G；输入3，您当前的剩余通话，
# 单位为分钟；输入0，退出自助查询系统。
print('-----------  输入1，显示您当前的余额； ------------\n'
      '-----------  输入2，显示您当前剩余的流量，单位为G； ------------\n'
      '-----------  输入3，您当前的剩余通话，单位为分钟； ------------\n'
      '-----------  输入0，退出自助查询系统。 ------------\n')
num = int(input("请根据上面的提示，输入你要查询的内容："))
while(num>=0 and num<=3):
    if num ==1:
        print('您的余额为：%.2f。'%123.23)
        break;
    elif num == 2:
        print('您当前剩余的流量为:%.2fG。'%10.88)
        break;
    elif num == 3:
        print('您当前的剩余通话为：%.2f分钟。'%56.90)
        break;
    elif num == 0:
        break;
    else:
        print('您的输入有误，请重新输入。')

# 8、几个好朋友一起玩逢七拍腿的游戏，即从1开始依次数数，当数到尾数为7的数或7的倍数时，则不报出该数，而是拍一下腿。现在编写程序，
# 从1数99，假设每个人都没有出错，计算共要拍多少次腿。
count = 0
for i in range(1,100):
    if i%10/7==1 or i%7==0:
        print('1到100内尾数为7或7的倍数有：%i：'%i)
        count = count + 1
print('尾数为7的数或7的倍数的数总共有：%d'%count)

# 9、输出2000-2020年之间的润年。
for i in range(2000,2030):
    if i % 4 == 0 and i % 100 != 0 or i%400==0:
        print('2000-2020年之间的润年:%d'%i)

# 10、由用户输入三个整数，判断这三个数是否可以构成三角形。如果可以构成三角形的话，
# 则进一步显示三角形的类型(等边，等腰，一般三角形)。
# 如果不构成三角形的话，则给出提示信息。
a = int(input('请输入三角形的第一条边：'))
b = int(input('请输入三角形的第二条边：'))
c = int(input('请输入三角形的第三条边：'))

if a+b>c and a-b<c:
    print('a,b,c可以构成三角形')
    if a==b or a==c or b==c:
      print('a,b,c构成的是等腰三角形')
    elif a == b == c:
      print('a,b,c构成的是等边三角形')
    else:
      print('a,b,c构成是一般三角形')
