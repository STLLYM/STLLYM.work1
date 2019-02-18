num=list(input("以 为间隔输入一个数组").split(" "))
for i in range(len(num)):
    num[i]=int(num[i])
for i in range(len(num)):
    if num[i]==0:
        num.append(num[i])
        num.pop(i)
print(num)
