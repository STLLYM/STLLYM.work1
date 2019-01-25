import time
def time_n():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)#暂停时间，单位秒，可以改变
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    #将时间转化为易读的格式应该就是格式化吧
