from threading import Lock, RLock
# Lock 互斥锁    效率高
# RLock 递归(recursion)锁  效率相对低
#
# l = Lock()
# l.acquire()
# print('希望被锁住的代码')
# l.release()
#
# rl = RLock()  # 在同一个线程中可以被acquire多次
# rl.acquire()
# rl.acquire()
# print('希望被锁住的代码')
# rl.release()    # 有多少次的acquire就要有多少次的release,要不然别人进不去

from threading import Thread, RLock as Lock

def func(i,lock):
    lock.acquire()
    lock.acquire()
    print(i,': start')
    lock.release()
    lock.release()
    print(i, ': end')

lock = Lock()
for i in range(5):
    Thread(target=func, args=(i, lock)).start()



