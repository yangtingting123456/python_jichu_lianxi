'''
@File : day02_08.py
@Time : 2021/1/31 16:41
@Author: luoman
'''
# import lib
# break ：结束本层循环
# continue：结束当次循环，继续进行下一次循环

for i in range(1, 11):
    if i == 5:
        break
    print(i, end='\t')

print()

for i in range(1, 11):
    if i == 5:
        continue
    print(i, end='\t')

# pass 占位语句
for i in range(1,12):
    pass

if 1>2:
    print('hello')
