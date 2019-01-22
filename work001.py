a_list=[1,2,3,4]                        #定义数组包含1，2，3，4四个元素
sum=0                                   #定义计数初始值
for i in range(len(a_list)):
    b_list=a_list.copy()                #使数组a_list不发生改变的同时将b_list使用调用获得a_list及其数据
    x=str(b_list.pop(i))                #以字符串形式将x赋予b_list.pop的返回值，方便后期直接将字符串表现
    for j in range(len(b_list)):        #重复上一个步骤只不过少了上次删除掉的数字
        c_list=b_list.copy()            
        y=str(c_list.pop(j))
        for k in range(len(c_list)):
            z=str(c_list[k])
            print(x+y+z)                #以字符串形式表示不同的三位数
            sum +=1                     #计算共有多少数字被以这种形式排列出来     
print("总数是%d"%sum)                   
     
