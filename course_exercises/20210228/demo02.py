def pri(n):
    if n>0:
        print('hello world')
        pri(n-1)
    else:
         pass

n1 = int(input('手动输入一个数字:') )
pri(n1)