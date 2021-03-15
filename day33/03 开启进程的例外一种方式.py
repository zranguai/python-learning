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
    print('主进程-->', os.getpid())
    for i in range(10):
        p = MyProcess(1, 2, 3)    # 传参数
        p.start()








