list1=[]
for x in range (100,1000):
    a=x//100
    b=x//10-a*10
    c=x%10
    if x==a**3+b**3+c**3:
        list1.append(x)
print(list1)
