
n=int(input())
a_list=[2]
if n==1:
    print("输入错误")
elif n==2:
    print("0")
elif n==3:
    print("1")
else:
    for i in range(3,n):
        flag=False
        for j in range(2,i):
            if i%j==0:
                flag=True
                break

        if flag==False:
            a_list.append(i)
    print(len(a_list))
