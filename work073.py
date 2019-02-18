x=list(input("以 为间隔输入一个数组nums:").split(" "))
y=int(input("target:"))
for i in range(len(x)):
    x[i]=int(x[i])
for i in range(len(x)):
    for j in range(len(x)):
        if x[i]==x[j]:
            pass
        else:
            if x[i]+x[j]==y:
                print(x[i],x[j])
