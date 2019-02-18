
n = 1
while n <= 7:
    a = int(input('input a number:\n'))
    while a < 1 or a > 50:
        print("请重新输入")
        a = int(input('input a number:\n'))
    print (a * '*')
    n += 1
