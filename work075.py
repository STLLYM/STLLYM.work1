x=input()
y=-1

for i in range(len(x)):
    if x.count(x[i])==1:
        y=i
        break
    else:
        pass
if y==-1:
    print(y)
else:
    print("第一个不重复的字符索引为%d"%y)
