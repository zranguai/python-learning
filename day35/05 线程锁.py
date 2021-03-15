from threading import Thread, Lock
n = 0
def add(lock):
    for i in range(500000):
        global n
        with lock:
            n += 1
def sub(lock):
    for i in range(500000):
        global n
        with lock:
            n -= 1

t_l = []
lock = Lock()
for i in range(2):
    t1 = Thread(target=add,args=(lock,))
    t1.start()
    t2 = Thread(target=sub,args=(lock,))
    t2.start()
    t_l.append(t1)
    t_l.append(t2)
for t in t_l:
    t.join()
print(n)


# import dis
# a = 0
# def func():
#     global a
#     a += 1
'''
锁
0 LOAD_GLOBAL
2 LOAD_CONST 
4 INPLACE_ADD
# GIL锁切换了
6 STORE_GLOBAL
释放锁
'''


from threading import Thread, Lock
import time
n = []
def append():
    for i in range(500000):
        n.append(1)
def pop(lock):
    for i in range(500000):
        with lock:
            if not n:
                time.sleep(0.0000001)    # 强制CPU轮转
            n.pop()

t_l = []
lock = Lock()
for i in range(20):
    t1 = Thread(target=append)
    t1.start()
    t2 = Thread(target=pop,args=(lock,))
    t2.start()
    t_l.append(t1)
    t_l.append(t2)
for t in t_l:
    t.join()
print(n)


# 不要操作全局变量,不要在类里操作静态变量 就不用加锁了
# += -= *= /= if while 数据不安全
# queue logging 数据安全的（内部已经实现了数据安全）


# dis callfunction store


