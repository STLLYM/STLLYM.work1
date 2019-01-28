x=list(input("输入一个五位数"))
if len(x)==5:
    if x[0]==x[-1]:
        if x[1]==x[-2]:
            print("这个五位数是回文数")
    else :
        print("这个数不是回文数")
else:
    print("输入错误")
