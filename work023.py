
a_list=[]
for i in range(2,1001):
    s=0
    for j in range(1,i):
        if i%j==0:
            s+=j
            if s==i:
                print(i)
#因为这道题与第十六到区别在于求其所有因数，而不是质因数，所以较十六题简单
