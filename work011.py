x=int(input())
def f(x):                              #方法1，使用将十进制数转化为二进制数
    a_list=[]                          #的数学方法，将分离得到的每一位放入数
    c=x                                #组中然后统计数组中有多少个数字1
    j=0
    while c>=1:
        d=c%2
        a_list.append(d)
        c=c//2
    a_list.reverse()    
    #  print (a_list)                  调试的时候用的，确定数字放入正确
    for i in range(len(a_list)):
        if a_list[i]==1:
            j+=1
    return j
print(f(x))

z=int(input())
def g(z):                              #方法2，直接用bin将其转化为二进制数之后
    m=0                                #由于其会带有0b所以将其转化为字符串形式
    t=str(bin(z))                      #判断其有多少“1”
    #print(len(t))
    for l in range (len(t)):
        if t[l]=='1':
            m+=1
    return m   
print(g(z))
