# 异常处理：处理软件或信息系统出现的异常状况
# 语法:try...except...else...finally
lista= [2,3,5]
try:  #监控下面可能出现错误的代码
    num=int(input('请输入下标：'))
    print(lista[num])
except IndexError as e: #多上面出错的代码进行处理
    print(e)
    print('下标越界')
except ValueError as e: #输入的值错误，进行错误
    print(e)
    print('输入的值错误')
except Exception as e:
    print(e)
else:
    print('未报错，执行语句')
finally:
    print('不管是否出错，都会执行')

print('异常处理之后运行')