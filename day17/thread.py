"""
-------------------------------------------------
   File Name:thread
   Author:Lee
   date: 2021/6/29-16:27
-------------------------------------------------
"""

import threading
import time


def a():
    print('我要吃饭了！')
    time.sleep(1)  # 让当前线程睡眠1s
    print('饭吃完了~')


def b():
    print('找对象聊聊天~')
    time.sleep(1)
    print('聊完了')


def c():
    print('我要追星,我要给爱豆点赞！')
    time.sleep(1)
    print('追星成功啦~')


start_time = time.time()  # 获取当前时间戳
a(), b(), c()  # 调用三个函数
end_time = time.time()
print('总共耗时:{}'.format(end_time - start_time))

print('===' * 50)


def a1():
    print('我不吃饭了！')
    time.sleep(1)  # 让当前线程睡眠1s
    print('以后都不吃了~')


def b1():
    print('找不到对象！')
    time.sleep(1)
    print('再努努力~')


def c1():
    print('再也不追星了！')
    time.sleep(1)
    print('以后也不追星了~')


start_time = time.time()

t1 = threading.Thread(target=a1)
t2 = threading.Thread(target=b1)
t3 = threading.Thread(target=c1)

t1.start()  # 启动线程  当前运行的程序代表主线程，t1、t2、t3代表子线程
t2.start()
t3.start()

end_time = time.time()
print('多线程运行总共耗时:{}'.format(end_time - start_time))
