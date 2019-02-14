a_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

x=int(input("请输入一个小于2^32的数字"))

#运算符号位
if x>=0:
    a_list[0]=0
else :
    a_list[0]=1
    x=-x

    
def f(x):                                                        
    c=x                                
    i=1
    while c>=1:
        d=c%2
        a_list[-i]=d
        c=c//2
        i+=1
f(x)
print(a_list)

for i in range(1,len(a_list)):
    a_list[i]=1-int(a_list[i])
print(a_list)
#如果需要再计算出值的话
m,n=1,0
while m<=len(a_list)-1:
    n+=int(a_list[-m])*2**(m-1)
    m+=1
print(n)
if a_list[0]==1:
    n=-n
print(n)

