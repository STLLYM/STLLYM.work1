def f(str1, str2):
  
    a_str1 = len(str1)
    b_str2 = len(str2)
    record = [[0 for i in range(b_str2+1)] for j in range(a_str1+1)] # 多一位
    maxNum = 0   # 最长匹配长度
    p=0
    for i in range(a_str1):
        for j in range(b_str2):
            if str1[i] == str2[j]:
    # 相同则累加
                record[i+1][j+1] = record[i][j] + 1
            if record[i+1][j+1] > maxNum:
     # 获取最大匹配长度
                 maxNum = record[i+1][j+1]
     # 记录最大匹配长度的终止位置
                 p = i + 1
    return str1[p-maxNum:p], maxNum
  
  
if __name__ == '__main__':
 str1 = input()
 str2 = input()
  
 a = f(str1, str2)
 print(a)
