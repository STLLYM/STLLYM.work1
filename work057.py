def a_list(n):
    l=[[1]]
    for i in range(n):
        l.append([1])                             #创建一个每个都以‘1’开头的二维列表
    for i in range(1,n):
        for x in range(1,i):
            l[i].append(l[i-1][x-1]+l[i-1][x])    #按照杨辉三角的规律将上一个二维列表中的元素加和放入新列表中
        l[i].append(1)                            #因为加和时没有最后一个数字，所以需要再最后加进去一个‘1’
    for i in range(n):                            
        print(l[i])                               #输出每一个子列表

n=int(input())
a_list(n)
