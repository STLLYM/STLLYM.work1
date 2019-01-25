import math
n=int(input())
list = [ ]                                     #建立一个列表存放分解出来的因数
                       
def g(n):                                      #用于分解因数的函数
    prise=True
    for i in range(2,int(math.sqrt(n))+1):     #因为在试数字时不需要到n而是到根号下n即可
        if n%i==0 and i!=n :                   #寻找第一个因数
            list.append(i)                     #并放入列表
            prise = False
            g(n/i)                             #再次引用函数寻找第二、三个因数
            break                              #在获得理论最后一个因数后打断避免重复全循环
    if prise:
        list.append(n)                         #最后一个的放入
 
g(n)                                           #引用刚刚设定好的函数
print(list)
j=0
for j in range(len(list)):                     #下边这些是为了打印成比较好看的形式
    print("%d*"%int(list[j]),end="")
if j==len(list)-1:
    print("1")
    
