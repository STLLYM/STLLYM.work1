m,n=3,3
a_list=[[0]*n]*m
print(a_list)
for i in range(m):
    a_list[i]=input("").split(",")
    for j in range(n):
        a_list[i][j]=int(a_list[i][j])


sum=0
for i in range(3):
    for j in range(3):
        if i==j:
            sum+=a_list[i][j]
print(sum)
            
