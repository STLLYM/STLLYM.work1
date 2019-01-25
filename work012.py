x=int(input("请输入一个整数"))
def f(x):
    i=0
    if x==0:
        return False
    while x%3==0:
        x=x//3                           #只有最后一次为x=1时才能够触发返回真值
        i+=1
    if x==1:
        print("这个数是3的%d次方"%i)
    return x==1
print(f(x))
