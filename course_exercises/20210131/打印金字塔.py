# 打印金字塔,i表示金字塔的行，j表示金字塔的列,k控制*打印的位置
#       *
#      * *
#     * * *
#    * * * *
num=int(input())
for i in range(1,num+1):
    print(' '*(num-i)+'*'*(2*i-1))
