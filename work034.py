a_list=list(input("请输入不多于5位的正整数"))
print("这是个%d位数"%len(a_list))
b_list=["个","十","百","千","万"]
for i in range(1,len(a_list)+1):
    print("%s位是%d"%(b_list[-i],int(a_list[i-1])))
