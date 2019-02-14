a=list(input("请以“，”为间隔输入三个数").split(','))
print("输入的数为",a)
print("则其由大到小的顺序为")
print(max(a))

b=min(a)

a.remove(max(a))
a.remove(min(a))
print(int(a[0]))
print(b)
#因为在最前边第几题那有三个数的比较，所以就没有写那边的方法
#因为么有更多的数，所以只有三个也可以用这种方法来比
