a_list=list(input("输入数组").split(" "))
b_list=list(input("输入数组").split(" "))
a_set=set(a_list)
b_set=set(b_list)

print("交集为：")
print(a_set & b_set )
