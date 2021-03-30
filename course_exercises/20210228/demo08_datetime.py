#日期时间
import datetime
#1、时间元组表示
t = datetime.datetime(2021,3,30,15,16,0,0)  #(年，月，日，时，分，秒，微妙)
#2、截取部分时间
print('年：',t.year)
print('月份：',t.month)
print('日期：',t.date())
print('小时：',t.hour)
print('分钟：',t.second)
print('几号：',t.day)
print('星期：',t.weekday())  #0到6
print('星期：',t.isoweekday())  #1到7
#3.获取当前系统时间
print('获取今天的时间：',datetime.datetime.today())
print('获取此刻的时间：',datetime.datetime.now())
#3.获取时间戳
print('t的时间戳是：',t.timestamp())  #将时间转换成时间戳
#4.将时间转换成字符串
print('t的时间字符串是：',t.fromtimestamp(t.timestamp()))
#5.按自定义格式返回字符串
print(t.strftime('将系统的时间自定义格式输出：','%Y-%m-%d %H:%M:%S'))  #注意中间的字符串不能随便修改
#
