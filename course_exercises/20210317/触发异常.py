# 异常分类：
# 1.系统异常：下标越界、值错误、路径错误。。。。
try:
    print('good good study,every every up')
    raise IndexError('我是下标越界错误!!!')#创建了一个错误对象
except IndexError as e:
    print(e)
print('good good study,every every up')

# 2.业务异常：充值只能是正数值、年龄范围1-120，账号密码错误。。。
#触发异常,由raise关键字触发的，只亚欧有raise就会报错
# eg：允许充值的范围0-100之间
#自定义一个业务异常类
class OnlyInputValue(Exception):
    def __str__(self):
        return '输入的充值范围只能是0-100之间的数字'

try:
    num = int(input('请输入0-100之间的数字：'))
    if num<0 or num>100:
        #手动触发异常
        raise OnlyInputValue()
    else:
        print('你输入的数是：{}'.format(num))
except OnlyInputValue as e:
    print(e)

except Exception as e:
    print(e)
    print('系统未知错误')


