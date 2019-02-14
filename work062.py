x=list(input("请以 为间隔输入一些数组").split(' '))
a=max(x)
b=min(x)
for i in range(len(x)):
    if x[i]==a:
        x[i]=x[0]
    elif x[i]==b:
        x[i]=x[-1]
x[0]=a
x[-1]=b

print(x)
