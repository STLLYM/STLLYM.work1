f = open("测试1.txt","w")
f.write("Lycoridiata\n")
f.write("wulei\n")
f.write("leilei\n")
f.write("Xingyu\n")
 
#两种方法实现把每一行文件以数组元素的形式放进数组中（split/splilines）
 
#其中spit是一个分割的作用，以'\n'为分割点，即把每一段分割成一个元素放入数组中
 
f = open("测试1.txt","r")
# print(f.read())
get = f.read()
result = get.split('\n')


#直接用splitlines（）放法来实现行分割
other_result = get.splitlines()
for i in range (len(other_result)):

 print(result[i])
 print("******")
 #print(other_result[i])
 #print("******")
 
f.close()
