dict1 = {'a':1,'c':2,'d':4,'b':3}
a=sorted(dict1.items(),key = lambda dict1:dict1[1],reverse = True)
print(a)
