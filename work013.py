x=int(input("输入第几月"))
def f(x):                             #类似与斐波那契数列只不过是需要*2
    if x==1 or x==2:                  #当然不考虑子代与亲代之间再产下新的子代
        sum=1
    else:
        sum=f(x-1)+f(x-2)
    return sum
a=f(x)*2
print (a)
