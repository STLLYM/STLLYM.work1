n=int(input())
a_list=[]
i=0
while i<n:
    i+=1
    a_list.append(str(i))
print(a_list)
for j in range( len(a_list) ):
    if (j+1)%3!=0 and (j+1)%5==0:
        a_list[j]=str('Buzz')
    elif (j+1)%3==0 and (j+1)%5!=0:
        a_list[j]=str('Fizz')
    elif (j+1)%3==0 and (j+1)%5==0:
        a_list[j]=str('FizzBuzz')
print(a_list)
#第一次写的时候a_list[j]=str('Buzz')里边忘记加‘’了所以错误了
