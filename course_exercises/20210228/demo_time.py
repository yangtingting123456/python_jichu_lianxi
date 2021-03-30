import time
#时间，日期
#time模块的常用的函数
#1.时间元组
#（年，月，日，时，分，秒，一周的第几日，一年的第几日，夏令日）
t = (2021,3,30,10,16,00,00,00,00)
#2.时间戳
print(time.time())   #获取当前时间戳
print(time.mktime(t))  #给点时间的时间戳
print(time.localtime(1617070631.4331083))   #讲时间戳转换成普通时间
#3.格式化显示(即时间字符串，时间元组相互转换)
print(time.strftime('%Y-%m-%d %H:%M:%p',time.localtime(time.time())))   #将时间元组按照一定的格式显示
print(time.strptime('2021-03-30 10:44:00','%Y-%m-%d %X'))   #
#4.英文显示
print(time.asctime(t))




#3.


#4.




import datetime
#datetime模块常用的函数