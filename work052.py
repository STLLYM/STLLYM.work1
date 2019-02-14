
#方法1，全程使用数学计算
a=int(input("请输入一个七位以上的数："))
a_list=[]
b,c,d=0,0,0
if a<1000000:
    print("请检查是否输入错误")
elif a<10000000:
    a=a//1000
else:
    b=a//1000
    c=b//10000
    a=b-10000*c
for i in range(1,5):
    d=(a%10**i)//10**(i-1)
    a_list.append(d)
print("从右端开始的4~7位为",a_list)
    

#方法2
x=list(input("请输入一个七位以上的数"))
for i in range(len(x)):
    x[i]=int(x[i])
if len(x)<7:
    print("请检查是否输入错误")
else:
    print("从右端开始的4~7位为")
    print(x[-4:-8:-1])
#好像，下边的简单一点
