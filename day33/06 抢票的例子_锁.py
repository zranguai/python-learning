# # 抢票的例子：加锁
# import json
# import time
# from multiprocessing import Process, Lock
#
#
# def search(i):
#     # 查询余票
#     with open('ticket', encoding='utf-8') as f:
#         ticket = json.load(f)
#     print(f'{i}:当前的余票为{ticket["count"]}张')
#
#
# def buy_ticket(name):
#     # 查询余票
#     with open('ticket', encoding='utf-8') as f:
#         ticket = json.load(f)
#     if ticket['count'] > 0:
#         ticket['count'] -= 1
#         print(f'{name}买到票了')
#     time.sleep(0.1)
#     with open('ticket', mode='w', encoding='utf-8') as f:
#         json.dump(ticket, f)
#
# def get_ticket(i, lock):
#     search(i)
#     with lock:    # 代替acquire和release 并在此基础上做一些异常处理，保证即便一个进程的代码出错了，也会归还钥匙
#         buy_ticket(i)
#     # lock.acquire()
#     # buy_ticket(i)
#     # lock.release()
# if __name__ == '__main__':
#     lock = Lock()    # 互斥锁
#     for i in range(10):
#         p = Process(target=get_ticket, args=(i, lock))
#         p.start()


# 锁：
# import time
# from multiprocessing import Lock, Process
# def func(i, lock):
#     lock.acquire()    # 拿钥匙
#     print(f'{i}被锁起来的代码')
#     # time.sleep(1)
#     lock.release()    # 还钥匙
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         p = Process(target=func, args=(i, lock))
#         p.start()

#  改动上面代码



# 为啥叫互斥锁？
from multiprocessing import Lock  # 互斥锁 不能再同一个进程中连续acquire多次
lock = Lock()
lock.acquire()
print(1)
lock.acquire()
print(2)



