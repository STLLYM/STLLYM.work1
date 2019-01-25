x=int(input("请输入您的分数"))
if x<=100 and x>=0:
    if x<90:
        if x <60:
            print("C")
        else:
            print("B")
    else:
        print("A")
else :
    print("输入错误")
