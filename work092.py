
x=0
for i in range(1,21):
    for j in range(1,51):
        if i*5+j*2<=100:
            n=100-i*5-j*2
            print("%d*5+%d*2+%d*1"%(i,j,n))
            x+=1
print(x)#这是总数
