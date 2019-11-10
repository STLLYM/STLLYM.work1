import math
n=int(input())
list1=[]

def f(n):
    flag=True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0 and i!=n :
            list1.append(i)
            flag=False
            f(n/i)
            break
    if flag:
        list1.append(n)

f(n)
print(list1)
