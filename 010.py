import time
def time_a():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time_a()
