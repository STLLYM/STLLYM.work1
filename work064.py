x=int(input('输入总人数：'))
a_list =list(range(1,x+1))
print(a_list)
n=0
while len(a_list)>1:
    b_list=a_list.copy()
    for i in range(len(b_list)):
        n+=1
        if n%3==0:
            a_list.remove(b_list[i])
print(a_list[0])
#在刚开始一直卡在删掉元素再如何排序的问题上，
#后来查找资料才发现一直排列到后边一直删就好了
