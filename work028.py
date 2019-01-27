x=int(input())
a_list=[]
def f(x):                               #两个斐波那契数列类型相除
    sum=0                               
    if x==1:                            
        sum=2                           
    elif x==2:                          
        sum=3                           
    else:
        sum=f(x-1)+f(x-2)
    return sum
#print(f(x))
def g(x):
    sum1=0
    if x==1:
        sum1=1
    elif x==2:
        sum1=2
    else:
        sum1=g(x-1)+g(x-2)
    return sum1
#print(g(x))               

a=0
for i in range(1,x+1):                   #将每个除完以后的值放入列表中
    a=f(i)/g(i)
    a_list.append(a)
#print(a_list)
print(sum(a_list))                       #对列表元素加和，输入20即为题目要求
    

