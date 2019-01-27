x=int(input())

for i in range(1,x+1):
    print(("* "*i).center((x+1)*5))
for i in range((x+1),0,-1):
    print(("* "*i).center((x+1)*5))
#这种方法画出来的菱形不是题目要求只是较为简洁，
#当然也可通过改字符串变为题目要求
#其中.center(x)是使.前边的字符串居中，两边补空格,总宽度为x



for i in range(1,x+1):
    for k in range(0,x-i):
        print(" ",end='')
        
    for j in range(i*2-1):
        print("*",end='')
    print()  
for i in range(2,x+1):
    for k in range(1,i):
        print(" ",end='')
    for j in range(2*(x+2-i)-3,0,-1):
        print("*",end='')
    print()
#额嗯，这种就得到题目所示菱形，
#后半部分完全是用数学公式试出来的range里边的范围        
