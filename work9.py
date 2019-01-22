
print("请输入楼梯数目")
x=int(input())
def fb(x):                       #嗯，在纸上演算了一下，好像是斐波那契数列类型
    if x==1:                     #所以就稍微改了一下然后用了
        sum=1
    elif x==2:
        sum=2
    elif x>=3:
        sum=fb(x-1)+fb(x-2)
    return su
print(fb(x))
