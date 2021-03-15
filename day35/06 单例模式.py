# 线程安全的单例模式要默写
import time
class A:
    from threading import Lock
    __instance = None
    lock = Lock()
    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                time.sleep(0.000001)    # cpu轮转
                cls.__instance = super().__new__(cls)
        return cls.__instance

def func():
    a = A()
    print(a)
from threading import Thread
for i in range(10):
    Thread(target=func).start()