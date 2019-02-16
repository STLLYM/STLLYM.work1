student_data = [[],[],[],[],[]]
x=5
data=[0,0,0]
def input_s(x):
    j=0
    while j<x:
        data[0] = input("输入学生号码：")
        data[1] = input("输入学生名字：")
        data[2] = input("输入学生分数：")
        student_data[j].extend(data)
        #print(student_data)
        j+=1

def output_s(x):
    for i in range(x):
        print(student_data[i][0],student_data[i][1],student_data[i][2])

if __name__=='__main__':
    input_s(x)
    print(student_data)
    output_s(x)
#这样可以是可以，但是就只能是五个，没法根据输入的人数
#添加初始二维数组的数目，待以后有机会学多再重新弄一下
