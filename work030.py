x=int(input("请输入你的数字数目："))
a_list=[]
for i in range(x):
    y=int(input("请输入数字："))
    a_list.append(y)
#print(a_list)
flag=False
for j in range(len(a_list)):
    for k in range(j+1,len(a_list)):
        if a_list[j]==a_list[k]:
            flag=True
            break  
if flag==True:
    print("true")
else:
    print("false")
#方法有一点取巧就是最后是打印出“true”和“false”
