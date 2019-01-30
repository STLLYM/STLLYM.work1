x=list(input("请以“ ”为间隔输入数组数字").split(" "))
#1输出为输入值按大小排列完之后再逆序
y=x.copy()
y.sort(reverse=True)
print("倒序之后为",y)
#2将输入直接逆序输出
z=x.copy()
z.reverse()
print("倒序之后为",z)
