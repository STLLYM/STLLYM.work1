

a_list=[]                              #在写的时候不小心把解表放到for循环
                                       #里边了，每一次都会重置，还好后来发现了
for i in range (101,200):
   
    k=0
    for j in range(2,i):
        flag=True
        if i%j==0:
            flag=False
            break
    if flag==True:
        a_list.append(i)
        
       
print(a_list)
print("共有%d个数"%len(a_list))
 
