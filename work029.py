x=int(input())
a_list=[]
a=1
for i in range(1,x+1):
    a*=i
    a_list.append(a)
#print(a_list)
print(sum(a_list))
    
