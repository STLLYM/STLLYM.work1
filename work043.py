x=list(input("以“，”为间隔输入一些数字").split(','))
y=[]
z=[]
for i in range(len(x)):
    x[i]=int(x[i])
y=x.copy()
y.sort()
print(y)
m=int(input())
for i in range(len(y)):
    if m<=y[i]:            #注意等号，一来防止列表中没有比较值，二来增加容错率
        y.insert(i,m)
        break              #一定要中止，不然会插入该数出现次数个m
print(y)
#以上是顺序排列时的插入
#以下是逆序排列时的插入
z=x.copy()
z.sort(reverse=True)       #当然其实可以对之前排列好的顺序列表倒序即可，但是本着练习原则
print(z)                   #复习了一下直接对列表倒序排列的方法
n=int(input())
for i in range(len(z)):
    if n>=z[i]:
        z.insert(i,n)
        break
print(z)
