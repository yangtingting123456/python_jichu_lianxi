# 编写后台管理员管理前台会员信息系统:
# 1. 后台管理员只有一个用户: admin, 密码: admin
# 2. 当管理员登陆成功后， 可以管理前台会员信息.
# 3. 会员信息管理包含:
#      添加会员信息
#      删除会员信息
#      查看会员信息
#      退出
# 界面如下，输入相应的数字进入相应的功能
# **********操作目录**********
#            1.添加会员信息
#            2.删除会员信息
#            3.查看会员信息
#            4.退出
#
# - 添加用户:
#    1). 判断用户是否存在?
#    2).  如果存在， 报错；
#    3).  如果不存在，添加用户名和密码分别到列表中;
#
# - 删除用户
#    1). 判断用户名是否存在
#    2). 如果存在，删除；
#    3). 如果不存在， 报错；
username = 'admin'
passwoed = 'admin'
usname = input("请输入用户名：")
psword = input("请输入密码：")
if username == usname and passwoed ==psword:
    print("**********操作目录**********")
    print("        1.添加会员信息       ")
    print("        2.删除会员信息       ")
    print("        3.查看会员信息       ")
    print("        4.退出              ")
    num=input("请输入对应的数字进入对应的模块：")
    if int(num) == 1:
        print("进入添加会员的模块")
        new_username = input("请输入你需要添加用户的用户名：")
        new_password = input("请输入密码：")
        if new_username == username:
            print('erro****你输入的用户名已经存在')
        else:
            print("添加成功")
            print("%s  %s"%(username,passwoed))
            print("%s  %s" % (new_username, new_password))
    elif int(num) == 2:
        print("进入删除会员的模块")
        delete_username = input("请输入你要删除的用户：")
        if delete_username == username:
            print("%s删除成功"%delete_username)
        else:
            print("erro****%s你删除的用户不存在"%delete_username)
    elif int(num) == 3:
        print("进入查看会员的页面，会员信息是，当前用户是%s"%username)
    elif int(num) == 4:
        print("退出成功")
    else:
        print("抱歉，你输入的数字没有对应的模块！")
else:
    print("用户名或密码错误")









