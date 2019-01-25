a_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
b_list=[]
x=int(input())
def f(x):                                                        
    c=x                                
    i=1
    while c>=1:
        d=c%2
        a_list[-i]=d
        c=c//2
        i+=1
f(x)
print(a_list)
a_list.reverse()
print(a_list)
m,n=1,0
while m<=len(a_list):
    n+=int(a_list[-m])*2**(m-1)
    m+=1
print(n)
#弄了半天才看懂题目的意思TAT 嗯这种用列表的方法比较笨但是比较好理解，比较深的
#方法之后有时间再学习加尝试
    
    
       
