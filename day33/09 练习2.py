# 练习1 实现进程的例外一种方式--面对对象
# from multiprocessing import Process
# import time
#
# class Myprocess(Process):
#     def __init__(self, a, b):    # 传递参数
#         self.a = a
#         self.b = b
#         super().__init__()
#     def run(self):
#         time.sleep(1)
#         print('My Process')
#         print(self.a, self.b)
#
# if __name__ == '__main__':
#     mp = Myprocess(1, 2)
#     mp.start()
#     mp.join()
#     print('in main')

# 练习2：守护进程
# from multiprocessing import Process
# import time
#
# def func():
#     print('in func start')
#     time.sleep(1)    # 到了时间片会切出来
#     print('in func')
#
# def foo():
#     print('in foo')
#
# if __name__ == '__main__':
#     p1 = Process(target=func)
#     p1.daemon = True
#     p1.start()
#     time.sleep(1)
#     p2 = Process(target=foo)
#     p2.start()
#     print('in main')

# 练习3：进程同步---锁
# from multiprocessing import Process, Lock
# import time
#
# def func(lock, i):
#     global n
#     lock.acquire()
#     time.sleep(0.2)
#     print(i)
#     lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         p = Process(target=func, args=(lock, i))
#         p.start()

# 练习4：生产者消费者模型---基于队列实现
# from multiprocessing import Process, Queue
# import time
#
# def consume(q):
#     while True:
#         food = q.get()
#         if food:
#             print(q.get())
#         else:
#             break
#
# def producer(q):
#     for i in range(1, 10):
#         print('produce-->', i)
#         q.put(i)
#         q.put('hehe')
#         q.put('haha')
#
# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=producer, args=(q, ))
#     p2 = Process(target=producer, args=(q, ))
#     c = Process(target=consume, args=(q, ))
#     c.start()
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)


























