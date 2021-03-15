import os
import time
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, a, b, c):    # 如果需要传参数，需要写__init__方法
        self.a = a
        self.b = b
        self.c = c
        super().__init__()    # 调用上级的__init__方法
    def run(self):    # 实现run的同名方法
        time.sleep(1)
        print(os.getppid(), os.getpid(), self.a)


if __name__ == '__main__':
    p = MyProcess(1, 2, 3)
    p.start()
    print(p.pid, p.ident)    # 查看子进程的pid  22672 22672(同)
    print(p.name)   # 查看子进程的名字
    print(p.is_alive())    # 查看进程是否活着
    p.terminate()   # 强制结束一个子进程    异步非阻塞
    print(p.is_alive())    # True? 因为操作系统响应需要一定时间
    time.sleep(0.01)
    print(p.is_alive())







