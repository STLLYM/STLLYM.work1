import os


def add(x,y):
    c=x+y
    return c
def sub(x,y):
    c=x-y
    return c
def mul(x,y):
    c=x*y
    return c
def div(x,y):
    c=x/y
    return c
def yunsuan():
    z=1
    a_list=list(input("请以 为间隔分别输入计算式的第一个数，运算符以及第二个数\n").split(' '))
    end = False
    for i in range(0,len(a_list),2):
        try:
            a_list[i]=int(a_list[i])
        except:
            print("输入了非法字符！")
            break
    if type(a_list[0])==int and type(a_list[2])==int:
        #print(type(a_list[0]))
        x=a_list[0]
        y=a_list[2]
        if a_list[1]=='+':
            end=add(x,y)
        elif a_list[1]=='-':
            end=sub(x,y)
        elif a_list[1]=='*':
            end=mul(x,y)
        elif a_list[1]=='/':
            if a_list[2]==0:
                print("输入错误，分母不为0.")
                end=False
            else:
                end=div(x,y)
    print("计算结果为",end)
    return end
z=0
print("***********************************")
print("************简单计算机**************")
print("***********************************")
a=1
while a!=0:
    #os.system('cls')

    yunsuan()
    print("继续计算请按任意键，退出请按0\n")
    a=input()

    if a=='0':
        break

print("已退出！")
