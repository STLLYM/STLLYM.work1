x=int(input())
y=int(input())
x,y=max(x,y),min(x,y)
print("较大的是%d,较小的是%d"%(x,y))


a_list=list(input("以 为间隔输入想比较的一堆数").split(" "))
a_list.sort()
print("其大小顺序为",a_list)
