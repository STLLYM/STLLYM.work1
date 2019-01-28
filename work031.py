x=int(input())
def f(x):
    sum=1
    if x==1:
        sum=1
    else :
        sum=x*f(x-1)
    return sum
f(x)
print(f(x))
