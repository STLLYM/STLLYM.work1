a_list=list(input().split(' '))
b_list=a_list.copy()
x=int(input("输入向后移动的位置数m："))
for i in range(x%len(b_list)):
    b_list.insert(0,b_list.pop())
print(b_list)
#与50有一点类似，然后将列表复制一下也只是习惯，其实直接用初始列表就可以
