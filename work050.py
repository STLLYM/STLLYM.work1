b_list=list(input("请以 为间隔输入一串数字").split(' '))
a_list=b_list.copy()
x=int(input("输入向右移动的位置数："))
y=int(input("输入您想要移动的元素："))
for i in range(len(a_list)):
    a_list[i]=int(a_list[i])
print("移动前为：",a_list)
for i in range(len(a_list)):
    #print(a_list)
    if y==a_list[i]:
        del a_list[i]
        a_list.insert(i+x,y)
        break
print("                第一个检索到的目标元素的移动为：")
print("移动后为：（当超出数组数量范围时将元素放于末尾）",a_list)
a=b_list.copy()
for i in range(len(a)):
    a[i]=int(a[i])
def f(a,x):
    for i in range(x%len(a)):
        a.insert(0,a.pop())
    return a
f(a,x)
print("全体元素向右移动x个长度为")
print(a)
