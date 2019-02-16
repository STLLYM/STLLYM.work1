n=int(input("请输入一个大于0的整数"))


def f(x):
    if x%2==0:
        i=2
        sum=0
        while i <= x:
            sum+=1/i
            i+=2
    else:
        i=1
        sum=0
        while i <= x:
            sum+=1/i
            i+=2
    return(sum)

            
print(f(n))
