x=int(input("年份为："))
y=int(input("月份为："))
z=int(input("日期为："))
i,sum=0,0

def years(x):
    flag=True
    if x%100!=0 and x%4==0 or x%100==0 and x%400==0:
        pass
    else:
        flag=False
    return flag

a_list=[31,28,31,30,31,30,31,31,30,31,30,31]
while i<y-1:
    sum+=a_list[i]
    i+=1
sum+=z
if years(x)==True:
    if y>2:
        sum+=1
        print(sum)
    else:
        print(sum)
else:
    print(sum)
        
    
