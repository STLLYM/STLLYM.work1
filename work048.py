x=int(input())
y=int(input())
t=0
t=x
x=y
y=t
print(x)
print(y)
#以上为方法1，引入第三个变量


#以下为方法2，直接交换赋值
x,y=y,x
print(x)
print(y)
