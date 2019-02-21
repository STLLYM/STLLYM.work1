x=list(input("以 为间隔输入一行数组").split(" "))
for i in range(len(x)):
    x[i]=int(x[i])

for j in range(0,max(x)):
    if x.count(j)==0:
        print(j)
        break
    
