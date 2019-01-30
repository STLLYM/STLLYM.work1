a_list=[2]
for i in range(3,101):
    flag=False
    for j in range(2,i):
        if i%j==0:
            flag=True
            break

    if flag==False:
        a_list.append(i)
print(a_list)
