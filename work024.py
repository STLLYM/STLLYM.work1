

x=int(input())
def f(x):
    h=100.0
    s=100.0
    for i in range (1,x):
        h=h/2
        s=s+2*h
    print("第%f次落地经过%f米"%(x,s))
    print("第%f次反弹高度为%f米"%(x,h/2))
    return 0

f(x)
#理论上这个可以求任意次数的反弹高度和路程，只要在精度内 定x=10 即为题目所求
