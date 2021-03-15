import time
from multiprocessing import Process

def son1():
    while True:
        print('--->in son1')
        time.sleep(1)


def son2():    # 10s
    for i in range(10):
        print('in son2')
        time.sleep(1)


if __name__ == '__main__':    # 3s
    p1 = Process(target=son1)
    p1.daemon = True    # 表示设置p1是一个守护进程  需要在start之前设置
    p1.start()
    p2 = Process(target=son2)
    p2.start()
    time.sleep(3)
    print('>>>>in main')
    p2.join()    # 等待p2结束之后才结束

# 等待p2结束 --> 主进程的代码才结束 --> 守护进程结束

# 主进程会等待所有的子进程结束，是为了回收子进程的资源
# 守护进程会等待主进程的代码执行结束之后再结束,而不是等待整个主进程结束
# 主进程的代码什么时候结束，守护进程就什么时候结束，和其他子进程的执行进度无关
#
#
# 要求守护进程p1必须再p2进程结束之后才结束








