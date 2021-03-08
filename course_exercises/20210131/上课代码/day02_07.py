'''
@File : day02_07.py
@Time : 2021/1/31 16:01
@Author: luoman
'''
# import lib

'''
5、	购物车 功能要求： 要求用户输入总资产，例如： 2000 ,显示商品列表，让用户根据序号选择商品，加入购物车 购买，
如果商品总额大于总资产，提示账户余额不足，否则，购买成功。 
 goods=[ {"name":"电脑","price":1999}, 
         {"name":"鼠标","price":10}, 
         {"name":"游艇","price":20}, 
         {"name":"美女","price":998}, 
]
'''
'''
# 简单版：一次买一个商品
goods=[{"name":"电脑","price":1999},
       {"name":"鼠标","price":10},
       {"name":"游艇","price":20},
       {"name":"美女","price":998}
       ]
money = int(input('请输入你的总资产:'))
# 显示商品列表
print('序号\t商品名称\t商品价格')
for i in goods:
    print('%d' % (goods.index(i)+1), end='\t')
    for key,value in i.items():
        print(value, end='\t\t')
    print('\n')
count = 0  # 购物车中的商品数量
index = int(input('请输入商品的序号:'))
buycount= 1  # 购买的商品数量
# 计算购买的商品金额
# 假设购买1号商品，实际上是goods商品表中的第0号元素
allprice  = goods[index-1].get('price') * buycount
print(allprice)
if money>=allprice:
    print('购买成功')
else:
    print('账户余额不足')
'''

# 进阶版：一次买一个商品，但是该商品数量可以是多个
'''
goods=[{"name":"电脑","price":1999},
       {"name":"鼠标","price":10},
       {"name":"游艇","price":20},
       {"name":"美女","price":998}
       ]
money = int(input('请输入你的总资产:'))
# 显示商品列表
print('序号\t商品名称\t商品价格')
for i in goods:
    print('%d' % (goods.index(i)+1), end='\t')
    for key,value in i.items():
        print(value, end='\t\t')
    print('\n')
count = 0  # 购物车中的商品数量
index = int(input('请输入商品的序号:'))
buycount= int(input("请输入商品的购买数量:"))
# 计算购买的商品金额
# 假设购买1号商品，实际上是goods商品表中的第0号元素
allprice  = goods[index-1].get('price') * buycount
print(allprice)
if money>=allprice:
    print('购买成功')
else:
    print('账户余额不足')
'''
# 高阶版：一次可以买多种商品，每种商品数量可以是多个
# 让他可以多次购物----循环---while:当不确定循环次数，但是知道循环退出的条件时， for：当确定循环次数的时候
goods=[{"name":"电脑", "price":1999},
       {"name":"鼠标", "price":10},
       {"name":"游艇", "price":20},
       {"name":"美女", "price":998}
       ]
money = int(input('请输入你的总资产:'))
allprice = 0
# 显示商品列表
while True: # 无条件进入循环
    print('序号\t商品名称\t商品价格')
    for i in goods:
        print('%d' % (goods.index(i)+1), end='\t')
        for key,value in i.items():
            print(value, end='\t\t')
        print('\n')
    count = 0  # 购物车中的商品数量
    index = int(input('请输入商品的序号:'))
    buycount= int(input("请输入商品的购买数量:"))
    # 计算购买的商品金额
    # 假设购买1号商品，实际上是goods商品表中的第0号元素
    allprice  = allprice +goods[index-1].get('price') * buycount
    print(allprice)
    e = input('是否继续购物？(任意键表示继续，n:去结算)')
    if e=='n':  # 使用这个条件结束循环
        break

if money>=allprice:
    print('购买成功')
else:
    print('账户余额不足')






