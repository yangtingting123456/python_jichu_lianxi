# 1、模拟简单的计算器，要求如下：
# 定义名为Number的类
# 其中有两个整型数据成员n1和n2
# 应声明为私有。编写构造方法：赋予n1和n2初始值
# 再为该类定义加（addition）、减（subtration）、乘（multiplication）、除（division）等公有成员方法
# 分别对两个成员变量执行加、减、乘、除的运算。
# 创建Number类的对象，调用各个方法，并显示计算结果。
class Number:
    def __init__(self,n1=8,n2=4):
        self.__n1 = n1
        self.__n2 = n2

    def addition(self):
        m1 = self.__n1+self.__n2
        print("n1和n2的和为：%s"%m1)

    def subtration(self):
        m2 = self.__n1 - self.__n2
        print("n1和n2的差：%s" % m2)

    def multiplication(self):
        m3 = self.__n1 * self.__n2
        print("n1和n2的乘积为：%s" % m3)

    def division(self):
        m4 = self.__n1 / self.__n2
        print("n1和n2除为：%s" % m4)

calculator = Number(8, 19)
calculator.addition()
calculator.subtration()
calculator.multiplication()
calculator.division()

# 2、创建一个学生类,属性：姓名，年龄，学号 方法：答到，展示学生信息,类属性：名称
#   创建一个班级类, 属性：学生，班级名 方法：添加学生，删除学生，点名
class Student():
    """学生"""
    def __init__(self,name='',age=0,id=''):
        self.name=name
        self.age=age
        self.id=id
    def answer(self):
        print('%s,到'% self.name)
    def show_info(self):
        print('姓名是:%s,年龄:%d,学号是%s'%(self.name,self.age,self.id))
class Class():
    """班级"""
    def __init__(self,name=''):
        self.name=name
        self.student=[]#里面是学生对象
        self.__num = 0

    def add_student(self):
        name = input('请输入学生的姓名:')
        age = input('请输入学生的年龄:')
        self.__num += 1
        id = 'python' + str(self.__num).rjust(3, '0')
        stu=Student(name,int(age),id)
        self.student.append(stu)

    def del_student(self):
        del_name=input('请输入要删除的学生姓名:')
        a = True
        for student in self.student[:]:
            if del_name==student.name:
                self.student.remove(student)
                print('删除成功!')
                a = False
        if a:
            print('没有该学生')

    def ask_name(self):
        """点名"""
        for student in self.student[:]:
            print(student.name)
            student.answer()

class1=Class('python1806')
for i in range(3):
    class1.add_student()
class1.del_student()
class1.ask_name()

# 3、设计一个车类，属性：车的类型、车的速度、
# 分别再建立两个子类：小汽车类、电动汽车类 去继承车类
# 为了实现汽车增加能源的方式，在父类中添加 一个增加能源方法 increased_energy() 做出抽象方法
# 实现小汽车类加 油  电动汽车充电的不同实现
from abc import ABCMeta,abstractmethod
class vehicle(metaclass=ABCMeta):
    def __init__(self,mold,speed):
        self.mold = mold
        self.speed =speed
    @abstractmethod
    def increased_energy(self):
        pass

class car(vehicle):
    def __init__(self,mold,speed):
        vehicle.__init__(self,mold,speed)

    def increased_energy(self):
        print(self.mold+"需要加油，速度才能达到%s"%self.speed)
car01 = car("小汽车",120)
car01.increased_energy()

class ElectricVehicles(vehicle):
    def __init__(self,mold,speed):
        vehicle.__init__(self,mold,speed)

    def increased_energy(self):
        print(self.mold+"需要充电，速度才能达到%s"%self.speed)

EV01 = ElectricVehicles("新能源汽车",90)
EV01.increased_energy()

# 4、设计一个数据类型类 DataType ,包含一个抽象方法 length 方法，
# 并建立多个子类（Dict、List、String、Tuple）对length 方法进行实现：
# 如Dict子类 实现length方法功能，输出显示“字典形式的数据，包含3个项”，依次类推
# 创建一个get_length方法，能实现传入不同的子类对象，输出不同的求长度的结果
from abc import ABCMeta,abstractmethod
class DataType(metaclass=ABCMeta):    #抽象类DataType
    @abstractmethod
    def length(self):     #抽象方法length
        pass

class Dict(DataType):
    def length(self):
        print('字典形式的数据，包含3个项')

    def get_length(self,object):
        return len(object.keys())

class List(DataType):
    def length(self):
        print('列表形式的数据，包含3个项')

    def get_length(self,object):
        return len(object)

class String(DataType):
    def length(self):
        print('字符串形式的数据，包含3个项')
    def get_length(self,object):
        return len(object)

class Tuple(DataType):
    def length(self):
        print('元组形式的数据，包含3个项')

    def get_length(self,object):
        return len(object)

dict = Dict()
dict01= dict.get_length({'id':23,'name':3,'value':2})
print(dict01)

dict = List()
dict01= dict.get_length([23,3,2,99,77])
print(dict01)

dict = Tuple()
dict01= dict.get_length((23,3,2,56,'iji'))
print(dict01)

dict = String()
dict01= dict.get_length('232')
print(dict01)

# 5、 写一个传奇游戏中的猪类，类中有属性：颜色、个头、攻击力、准确度。有一个展示猪信息的方法。
# 再写一个测试类，生成一个猪的对象，将此猪的颜色值为“白色”，个头为5厘米，攻击力为50点血，准确度为0.8。
# 要求输出此猪的信息格式为：一只白色的猪，个头5厘米，攻击为为50点血，准确度为0.8，我好怕怕呀
class Pig:
    def __init__(self,color,height,aggressivity,accuracy):
        self.color = color
        self.height = height
        self.aggressivity = aggressivity
        self.accuracy = accuracy

    def show_pig_infos(self):
        print("一只%s的猪,个头为%s厘米，攻击力为%s点血,准确度为%s，我好怕怕呀"%(self.color,self.height,self.aggressivity,self.accuracy))

if __name__ == '__main__':
    white_pig = Pig("白色",5,50,0.8)
    white_pig.show_pig_infos()

# 6、 写一个牌的类，类中有属性：花色、值。有一个展示牌信息的方法。
# 要求写一个测试类，生成一张牌，将此牌的花色设为“梅花”，将此牌的值设为5。
# 最后显示此牌的信息，要求格式为:梅花5
class plate:
    def __init__(self,color,value):
        self.color = color
        self.value = value

    def shows(self):
        print(self.color+self.value)

if __name__ == '__main__':
    pai  = plate("梅花","5")
    pai.shows()

# 7、 写一个猪类，类中的属性：品种，颜色，攻击力。类中有方法：无返回值的方法：
#     （一）猪走路的方法，没有返回值，要求输出格式为“某某品种的某某颜色的猪走来走去”。
#     （二）猪打人的方法，没有返回值，要求输出格式为“某某品种的某某颜色的猪打人了，攻击力为多少”。
#     (三）猪吃饭的方法，没有返回值，要求输出格式为“某某品种的某某颜色的猪吃得真多”。
#     有返回值的方法：
#     （一）显示自身信息的方法（show_info)。
#     （二）得到此猪品种的方法，要求在此方法中没有输出，返回此猪的品种。
#     （三）得到此猪颜色的方法，要求在此方法中没有输出，返回此猪的颜色。
class Pig:
    def __init__(self,bread,color,aggressivity):
        self.bread = bread
        self.color = color
        self.aggressivity = aggressivity

    def pig_walk(self):
        print("%s品种的%s颜色的猪走来走去"%(self.bread,self.color))

    def pig_fight(self):
        print("%s品种的%s颜色的猪打人了，攻击力为%s"%(self.bread,self.color,self.aggressivity))

    def pig_eat(self):
        print("%s品种的某某颜色的猪吃得真多"%self.bread)

    def show_info(self):
        return "haha,来了一只%s品中的猪，战斗力为%s"%(self.bread,self.aggressivity)

    def get_bread(self):
        return self.bread

    def get_aggressivity(self):
        return self.aggressivity

red_pig = Pig("荷兰","red",0.8)
red_pig.pig_eat()
red_pig.pig_walk()
red_pig.pig_fight()
red_pig.show_info()
print("这只猪的品种为："+red_pig.get_bread())
print("这只猪的战斗力为：",red_pig.get_aggressivity())

# 8、 写一个汽车的类，类中有属性：品牌，价格，颜色。类中有方法：
#     （一）显示当前汽车对象的所有属性的方法show_info。
#     （二）汽车启动的方法，要求输出“XX品牌的汽车启动了”。
#     （三）汽车加速的方法，要求输出“XX品牌的汽车加速中”。
#     （四）汽车被卖的方法，要求输出“XX品牌的汽车被以XX元的价格卖了”。
class Automobile:
    def __init__(self,bread,price,color):
        self.bread = bread
        self.price = price
        self.color = color

    def show_info(self):
        print("这辆汽车的品牌为：%s,价格为：%s,颜色为：%s"%(self.bread,self.price,self.color))

    def firing(self):
        print("%s品牌的汽车启动了"%self.bread)

    def speed_up(self):
        print("%s品牌的汽车加速中"%self.bread)

    def be_sold(self):
        print("%s品牌的汽车被以%s元的价格卖了"%(self.bread,self.price))

Automobile_01 = Automobile("本田",150000,"black")
Automobile_01.show_info()
Automobile_01.firing()
Automobile_01.speed_up()
Automobile_01.be_sold()
