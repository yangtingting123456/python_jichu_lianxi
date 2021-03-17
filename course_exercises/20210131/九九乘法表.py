# 打印九九乘法表, i:控制行    j：控制列
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d' % (j,i,i*j),end='\t')
    print('\n')
