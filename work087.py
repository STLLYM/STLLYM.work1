n=input("请输入n个字符").split(" ")
a_list=list(input("输入n个新字符").split(" "))
a_dict={}
for i in range(len(n)):
    a_dict[n[i]]=a_list[i]
print (a_dict)
