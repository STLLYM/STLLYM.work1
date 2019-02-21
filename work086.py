f1=open ("f1.txt","w")
f1.write("azasd")
f1.close()
f1=open ("f1.txt","r")
str1=f1.read()
print(str1)
f1.close()


f2=open ("f2.txt","w")
f2.write("skrskr")
f2.close()
f2=open ("f2.txt","r")
str2=f2.read()
print(str2)
f2.close()


str3=str1+str2
print(str3)
list1=[]
for i in range(len(str3)):
    list1.append(str3[i])
list1.sort()
print(list1)
#print(type(list1[1]))


f3=open("f3.txt",'w')
for i in range(len(list1)):
    f3.write(list1[i])
f3.close()

