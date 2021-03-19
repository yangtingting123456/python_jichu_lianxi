# 模拟简单的计算器，要求如下：
# 定义名为Number的类
# 其中有两个整型数据成员n1和n2
# 应声明为私有。编写构造方法：赋予n1和n2初始值
# 再为该类定义加（addition）、减（subtration）、乘（multiplication）、除（division）等公有成员方法
# 分别对两个成员变量执行加、减、乘、除的运算。
# 创建Number类的对象，调用各个方法，并显示计算结果。
class Number:
    def __init__(self,n1,n2):
        self.__n1 = n1
        self.__n2 = n2

    def addition(self):
        return self.__n1+self.__n2

    def subtration(self):
        return self.__n1-self.__n2

    def multiplication(self):
        return self.__n1*self.__n2

    def division(self):
        return self.__n1/self.__n2

number1 = Number(4,2)
print('两数相加的和为：', number1.addition())
print('两数相减的差为：', number1.subtration())
print('两数相除的商为：', number1.division())
print('两数相乘的乘积为：', number1.multiplication())

# 定义名为MyTime的类：
# 其中应有三个整型成员：时（hour）、分（minute）、秒（second）
# 1）为了保证数据的安全性，这三个成员变量应声明为私有。
# 2）为MyTime类定义构造方法，以方便创建对象时初始化成员变量。
# 3）再定义diaplay方法，用于将时间信息打印出来。
# 4）为MyTime类添加以下方法addSecond(int sec) addMinute(int min) addHour(int hou) subSecond(int sec)
# subMinute(int min) subHour(int hou) 分别对时、分、秒进行加减运算。
# 5）定义封装的get和set方法，方便另外一个类对三个私有变量进行使用，并写成另外类如何调用该方法
class MyTime:
    def __init__(self,hour,minute,second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def set_Hour(self,hour):
        self.__hour = hour

    def get_hour(self):
        return self.__hour

    def set_minute(self,minute):
        self.__hour = minute

    def get_minute(self):
        return self.__minute

    def set_second(self,second):
        self.__hour = second

    def get_second(self):
        return self.__second

    def diaplay(self):
        print("时：%d，分：%d，秒：%d"%(self.__hour,self.__minute,self.__second))

    def addSecond(self,sec):
        sec = sec + self.__second
        return sec

    def addMinute(self,min):
        min = min + self.__minute
        return min

    def addHour(self,hou):
        hou = hou + self.__hour
        return hou

    def subSecond(self,sec):
        sec = sec-self.__second
        return sec

    def subMinute(self,min):
        min = min - self.__minute
        return min

    def subHour(self,hou):
        hou = hou - self.__hour
        return hou

time_01 = MyTime(12,45,23)
time_01.diaplay()
print('时：',time_01.get_hour())
print('分:',time_01.get_minute())
print('秒：',time_01.get_second())
print(time_01.addHour(21))
print(time_01.subHour(19))
print(time_01.addMinute(22))
print(time_01.subMinute(300))
print(time_01.addSecond(55))
print(time_01.subMinute(380))

# 设计一个交通工具类vehicle，其中的属性包括速度speed、种类kind、颜色color；方法包括：设置颜色setColor，取得颜色getColor。
# 再设计一个子类Car，增加属性passenger表示可容纳旅客人数，添加方法取得最大速度getMaxSpeed()。对两个类都进行初始化构造 创建Car的对象，输出Car的所有属性
class Vehicle:
    def __init__(self,speed,kind,color):
        self.speed = speed
        self.kind = kind
        self.color = color

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color

class Car(Vehicle):
    def __init__(self,speed,kind,color,passenger):
        super(Car, self).__init__(speed,kind,color)   #继承vehicle的属性
        self.passenger = passenger

    def getMaxSpeed(self):
        return self.speed

car01 = Car(120,'丰田','红色',7)
print(car01.speed)
print(car01.kind)
print(car01.getColor())
print(car01.passenger)

# 创建一个父类Animal类,属性：姓名、动物种类、年龄、性别,方法：吃
# 在父类的基础上创建两个子类 Dog cat ，新有尾巴、奔跑速度属性,新有方法：跑  叫
# 要求，新建对象时所有的属性都能进行初始化
class Animal:
    def __init__(self,name, kind, age, sex):
        self.name = name
        self.kind = kind
        self.age = age
        self.sex = sex

    def eat(self):
        print('我叫%s,我是%s的动物,我今年%d岁了，我的性别是%s'%(self.name,self.kind,self.age,self.sex))

class Dog(Animal):
    def __init__(self,name,kind,age,sex,tail,speed):
        super(Dog, self).__init__(name,kind,age,sex)
        self.tail = tail
        self.speed = speed

    def run(self):
        print('cat is  run now,speed is %s' % self.speed)

    def shout(self):
        print('Dog is shout now,I %s' % self.tail)

class Cat(Animal):
    def __init__(self,name,kind,age,sex,tail,speed):
        # super(Cat, self).__init__(name,kind,age,sex)
        Animal.__init__(self,name,kind,age,sex)
        self.tail = tail
        self.speed = speed

    def run(self):
        print('cat is  run now,speed is %s'%self.speed)

    def shout(self):
        print('Dog is shout now,I  %s'%self.tail)

dog01 = Dog('小黄','大犬',3,'雄性','无尾巴',20)
dog01.eat()
dog01.run()
dog01.shout()

dog01 = Cat('小黄','波斯',3,'雌性','有尾巴',20)
dog01.eat()
dog01.run()
dog01.shout()

# 1、在异常处理中这些try、except、else、finally、raise有什么含义
# try:捕捉异常代码
# except:处理捕捉异常的代码，使程序继续运行
# finally:不管是否报错都会执行
# else：不报错执行
# raise：手动引发的异常
list = [1,2,4,5]
try:
    a = list[29]
except IndexError as e:
    print(e)
else:
    print('else....')
finally:
    print('finally....')
#
# def error(Exception):
#     raise Exception

# 2、创建一个用户自定义异常UsernameInputError,如果用户用户名输入错误，能通过捕获错误并提示用户名***输入错误
class UsernameInputError(ValueError):
    pass
name = 'admin'
username = input('请输入您的用户名：')
if name == username:
    print('login success')
else:
    raise UsernameInputError('用户名%s输入错误'%username)

# 3、调研完成python读取 .ini文件
f = open("D:\\PycharmProjects\\python_jichu_lianxi\\homework\\20210317\\homework_p7杨婷婷_20210317.py",
         "r",encoding='utf-8')
print(f.read())
f.close()

