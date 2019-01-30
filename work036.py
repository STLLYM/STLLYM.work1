x=input("请输入星期的首字母：")
if x=='M':
    print("这是星期一")
elif x=='T':
    y=input("请输入星期的第二个字母：")
    if y=='h':
        print("这是星期四")
    elif y=='u':
        print("这是星期二")
    else:
        print("输入错误")
elif x=='W':
    print("这是星期三")
elif x=='F':
    print("这是星期五")
elif x=='S':
    z=input("请输入星期的第二个字母：")
    if z=='a':
        print("这是星期六")
    elif z=='u':
        print("这是星期天")
    else:
        print("输入错误")
else:
    print("输入错误")
