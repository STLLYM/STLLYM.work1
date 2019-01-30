m,n=3,3
a_list=[[1]*m]*n
for i in range(m):
    a_list[i]=input("").split(" ")
    for j in range(n):
        a_list[i][j]=int(a_list[i][j])
print("矩阵1为")
print(a_list[0])
print(a_list[1])
print(a_list[2])
b_list=[[1]*m]*n
for i in range(m):
    b_list[i]=input("").split(" ")
    for j in range(n):
        b_list[i][j]=int(b_list[i][j])
print("矩阵2为")
print(b_list[0])
print(b_list[1])
print(b_list[2])
c_list=[[0]*m]*n
for i in range(m):
    for j in range(n):
        c_list[i][j]=a_list[i][j]+b_list[i][j]
print("对应位置加和后的新矩阵为")
print(c_list[0])
print(c_list[1])
print(c_list[2])


