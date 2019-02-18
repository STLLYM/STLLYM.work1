a=[]
for i in range(0,4):
    x=int(input("输入第%d位数"%(i+1)))
    a.append((x+5)%10)
#print(a_list)
a[0],a[3]=a[3],a[0]
a[1],a[2]=a[2],a[1]
print("数据为",a)
