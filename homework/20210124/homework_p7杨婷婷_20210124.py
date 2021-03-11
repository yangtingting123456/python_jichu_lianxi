# 1.	给定一个非空正整数的列表，按照列表内数字重复出现次数，从高到低排序
int_list = [2,3,4,2,2,5,6,6,3,2,1,1,2,3]
dict_key = {}
for i in range(1,7):
    dict_key.update({i: int_list.count(i)})
print(dict_key)
sorted_list = sorted(dict_key.items(),key=lambda x:x[1],reverse=True)
print(sorted_list)
for i in sorted_list:
    print(i)

# 2.	月份缩写：如果有 months = "Jan.Feb.Mar.Apr.May.Jun.Jul.Aug.Sep.Oct.Nov.Dec."，
# 编写一个程序，用户输入一个月份的数字，输出月份的缩写。
mouths = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
get_keys =list(mouths.keys())
print(get_keys)
get_values= list(mouths.values())
print(get_values)
input_mounth = int(input())
if input_mounth in get_keys:
    print(get_values[input_mounth-1])
else:
    print('sorry,你输入的月份不存在！')

# 3、定义列表：
# L = [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'],['Adam', 'Bart', 'Lisa']]
# 请分别取出['Apple', 'Google', 'Microsoft’]、’Ruby’,[‘Adam’,’Bart’]
# a.计算列表长度并输出
# b.列表中追加元素"seven"，并输出添加后的列表
# c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
# d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
L = [['Apple', 'Google', 'Microsoft'],['Java', 'Python', 'Ruby', 'PHP'],['Adam', 'Bart', 'Lisa']]
L0 = L[0]
L1 = L[1][2]
L2 = L[2]
L3 = []
for i in range(0,2):
    L3.append(L[2][i])
print(L0,L1,L3)
print(len(L))
L.append('seven')
print(L)
L.insert(0,'Tony')
print(L)
L[1] ='kelly'
print(L)

# 4.	写代码，有如下列表，按照要求实现每一个功能：
# li = ['alex','eric','rain']
# a.计算列表长度并输出
# b.列表中追加元素"seven"，并输出添加后的列表
# c.请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
# d.请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
# e.请删除列表中的元素"eric"，并输出修改后的列表
# f.请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
# g.请删除列表中的第3个元素，并输出删除元素后的列表
# h.请删除列表中的第2至4个元素，并输出删除元素后的列表
# i.请将列表所有的元素反转，并输出反转后的列表
# j.请使用for、len、range 输出列表的索引
# k.请使用enumrate输出列表元素和序号（序号从 100 开始）
# l.请使用for循环输出列表的所有元素
#计算列表长度并输出
l1=['alex', 'eric', 'rain']
print(len(l1))
#列表中追加元素“seven”，并输出添加后的列表
l1 = ['alex', 'eric', 'rain']
l1.append('seven')
print(l1)
#请在列表的第1个位置插入元素“Tony”，并输出添加后的列表
l1 = ['alex', 'eric', 'rain']
l1.insert(0,'Tony')
print(l1)
#请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
l1 = ['alex', 'eric', 'rain']
l1[1]='Kelly'
print(l1)
#请删除列表中的元素“eric”，并输出修改后的列表
l1 = ['alex', 'eric', 'rain']
l1.remove('eric')
print(l1)
#请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
l1 = ['alex', 'eric', 'rain']
l1.pop(1)
print(l1)
#请删除列表中的第3个元素，并输出删除元素后的列表
l1 = ['alex', 'eric', 'rain']
del l1[2]
print(l1)
#请删除列表中的第2至4个元素，并输出删除元素后的列表
l1 = ['alex', 'eric', 'rain']
del l1[1:4]
print(l1)
#请将列表所有的元素反转，并输出反转后的列表
l1 = ['alex', 'eric', 'rain']
l1.reverse()
print(l1)
#请使用for、len、range输出列表的索引
l1 = ['alex', 'eric', 'rain']
for i in range(len(l1)):
    print(i)
#请使用enumrate输出列表元素和序号（序号从100开始）
l1 = ['alex', 'eric', 'rain']
for k,v in enumerate(l1,100):
    print(k,v)
#请使用for循环输出列表的所有元素
for i in l1:
    print(i)

# 5、	购物车功能要求：要求用户输入总资产，
# 例如： 2000显示商品列表，让用户根据序号选择商品，加入购物车购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
goods=[{"name":"电脑","price":1999},{"name":"鼠标","price":10},{"name":"游艇","price":20},{"name":"美女","price":998}]
total_money = input('请输入您的总资产：')
goods_name = []
for i in range(0,len(goods)):
    goods_name.append(goods[i]['name'])
goods_price= []
for i in range(0,len(goods)):
    goods_price.append(goods[i]['price'])
for i in range(0,len(goods_name)):
    print('****%d---%s*****'%(i,goods_name[i-1]))
input_number = input('请输入您要购买的商品的序号：')
input_goods_number = list(input_number)
for i in range(0,len(input_goods_number)):
    total_goods_money =0
    total_goods_money = goods_price[i] +total_goods_money
if int(total_money)<int(total_goods_money):
    print('账户余额不足')
else:
    print('购买成功')










