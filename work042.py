m,n=3,3
b_list =[[0]*m]*n
for i in range(m):
    b_list[i]=input("请以“ ”为间隔输入三个数").split(" ")
    for j in range(n):
        b_list[i][j]=int(b_list[i][j])  #整形一下，方便加和
print(b_list[0])
print(b_list[1])
print(b_list[2])
sum=0
for i in range(3):
    for j in range(3):
        x=b_list[i]          #先将对应列表放入x中
        y=x[j]               #再将对应值赋给y
        if i==j:             #判断i与j相等时是对角线上的值
            sum += y         #加和并赋给sum
print(sum)
#可以通过改参数变为其他列表以及求其它列或行的和
