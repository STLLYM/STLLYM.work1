a=int(input("请输入想要加的数："))
x=int(input("请输入要加的层数即几个数相加："))
i,b=0,0
c_list=[]
while i < x:
    b+=a*10**i
    i+=1
    c_list.append(b)
print(c_list)
print(sum(c_list))
