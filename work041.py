list1=list(input("请以“，”为间隔输入数字").split(","))

list2=[]
for i in range(len(list1)):
    list2.append(int(list1[i]))
list2.sort()
print(list2)


list2.sort(reverse=True)
print(list2)

#以逗号为间隔输入十个数字即为顺序和倒序排列了
