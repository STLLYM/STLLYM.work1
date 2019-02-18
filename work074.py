x=int(input("输入猴子的数目："))
i,j=1,1
while j <= x:
    i=i*5+1
    j+=1
print(i)
#因为是求最少所以i定为1，可以定的大一些
#x定位5为题目所求
