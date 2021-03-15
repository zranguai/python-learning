# 练习1：生产者，消费者模型
# from multiprocessing import Process, Queue
# import time
# import random
# def consumer(q, name):
#     while True:
#         food = q.get()
#         if food:
#             print(f'{name}吃了{q.get()}')
#         else:
#             break
#
#
# def producer(q, name, food):
#     for i in range(10):
#         foodi = f'{food}{i}'
#         print(f'{name}生产{foodi}')
#         time.sleep(random.random())
#         q.put(foodi)
#
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=consumer, args=(q, 'alex'))
#     p1 = Process(target=producer, args=(q, '大壮', '苹果'))
#     p2 = Process(target=producer, args=(q, '雪飞', '香蕉'))
#     c1.start()
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
