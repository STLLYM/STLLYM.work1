a_list=list(input("请输入一行字符："))
l_list=[]
n_list=[]
s_list=[]
o_list=[]


for i in range(len(a_lsit)):
    if ord(a_list[i]) in range(65,91) or ord(a_list[i]) in range(97,123):
        l_list.append(a_list[i])
    elif a_list[i] ==' ':
        s_list.append(' ')
    elif ord(a_list[i]) in range(48,58):
        n_list.append(a_list[i])
    else:
        o_list.append(a_list[i])

print("英文字母个数为%d"%len(l_list))
print("数字个数为%d"%len(n_list))
print("空格个数为%d"%len(s_list))
print("其他字符个数为%d"%len(o_list))



#补充说明，由于字符中涉及种类较多，则可以由统一的ASCII码计数，转换函数ord,其中
#   0~9-->48~57
#   A~Z-->65~90
#   a~z-->97~122
