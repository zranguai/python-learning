# 进程之间数据隔离---队列
# 进程之间通信(IPC) Inter Process communication
#     基于文件：同一台机器上的多个进程之间的通信
#         Queue队列
#             基于socket的文件级别的通信来完成数据传递的
#     基于网络：同一台机器或者多台机器上的多进程间通信
#         第三方工具（消息中间件）
#             memcache
#             redis
#             rabbitmq
#             kafka

# from multiprocessing import Queue, Process
#
# def pro(q):
#     for i in range(11):
#         print('--->', q.get())
# def son(q):
#     for i in range(10):
#         q.put(f'hello{i}')
#
# if __name__ == '__main__':
#     q = Queue()
#     Process(target=son, args=(q, )).start()
#     Process(target=pro, args=(q, )).start()


# 生产者消费者模型  背下来
#     爬虫的时候
#     分布式操作：celery
#     本质：就是让生产数据和消费数据的效率达到平衡并且最大化的效率

from multiprocessing import Queue, Process
import time
import random

def consumer(q, name):  # 消费者: 通常取到数据之后还要进行某些操作
    while True:
        food = q.get()
        if food:
            print(f'{name}吃了{q.get()}')
        else:
            break


def producer(q, name, food):  # 生产者：通常再放数据之前先通过某些代码来获取数据
    for i in range(10):
        foodi = f'{food}{i}'
        print(f'{name}生产了{foodi}')
        time.sleep(random.random())
        q.put(foodi)

if __name__ == '__main__':
    q = Queue()
    c1 = Process(target=consumer, args=(q, 'alex'))
    p1 = Process(target=producer, args=(q, '大壮', '苹果'))
    p2 = Process(target=producer, args=(q, 'b哥', '梨子'))
    c1.start()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    q.put(None)    # 有多少个消费者就put多少个None进来

