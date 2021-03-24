# 1、将python所学内容整理成思维导图
# 2、自己完成以下研究
# 2.1 python连接MySQL数据库进行数据的操作
import pymysql.cursors
# 打开数据库连接
connection = pymysql.connect(host="192.168.177.42",port=3306,user="root",
                     password="Php123&juneyaokc",db="interface_test_db",
                             charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
sql = 'select * from api_test'
cursor.execute(sql)
result = cursor.fetchone()
print(result)
connection.close()
# 2.2 python实现发送邮件
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '2656343994@qq.com'  # 发件人邮箱账号
my_pass = 'jgvwxssjkhcddihi'  # 发件人邮箱密码
my_user = '3048903923@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")