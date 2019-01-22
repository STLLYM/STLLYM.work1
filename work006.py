print("输入一个数字，得到一个斐波那契数列")


x=int(input())
num_list=[]
def num(x):
    if x>=3:
        sum=num(x-1)+num(x-2)
    else :
        sum=1
    return sum
for i in range (0,x):
    num_list.append(num(i+1))
print(num_list)


y=int(input())
num_list2=[]
def num1(y):
    if y==1 or y==2:
        su=1
    else:
        su=num1(y-1)+num1(y-2)
    return su
for j in range (y):
    num_list2.append(num1(j+1))
print(num_list2)


z=int(input())
num_list3=[]
def num2(z):
    a,b=1,1
    if z==1 or z==2:
        return 1
    else:
        i=3
        while i<=z:
            a,b=b,a+b
            i+=1
        return b
for k in range(0,z):
    num_list3.append(num2(k+1))
print(num_list3)
print("最后一位是%d"%num2(z))
