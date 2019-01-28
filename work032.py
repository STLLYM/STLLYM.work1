x=input()
def f(x):
    if len(x)>0:
        print(x[-1])
        return f(x[0:-1])
        
f(x)
#注意运用切片
