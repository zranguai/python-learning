# 有多少个任务就开多少个进程或者线程
# 什么是池？
#     要在程序开始的时候，还没提交任务先创建几个进程或者线程
#     放在一个池子里，这就是池，放线程就是线程池，放进程就是进程池
#
# 为什么要用池?
#     如果先开好进程/线程,那么有任务之后就可以直接使用这个池中的数据了
#     并且开好的线程或者进程会一直存在在池中,可以被多个任务反复利用
#         这样极大的减少了开启\关闭\调度线程/进程的时间开销
#     池中的线程/进程个数控制了操作系统需要调度的任务个数,控制池中的单位
#         有利于提高操作系统的效率,减轻操作系统的负担
# 发展过程
# threading模块 没有提供池
# multiprocessing模块 仿照threading写的 Pool
# concurrent.futures模块 线程池,进程池都能够用相似的方式开启\使用

# 线程池：
# import time
# import random
# from threading import current_thread
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
# def func(a, b):
#     print(current_thread().ident, 'start', a, b)
#     time.sleep(random.randint(1, 4))
#     print(current_thread().ident, 'end')
#
# # 先开4个线程，其中有线程结束时会有新的线程进去，始终使用开启的4个线程
# if __name__ == '__main__':
#     tp = ThreadPoolExecutor(4)    # 在该线程池中开4个线程
#     for i in range(10):
#         tp.submit(func, i, i+1)    # (传递参数) 把任务提交给池，池替你执行线程中的任务


# 实例化 创建池
# 向池中提交任务，submit 传参数（按位置传，按关键字传）



# 进程池：
# import time
# import random
# import os
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
# def func(a, b):
#     print(os.getpid(), 'start', a, b)
#     time.sleep(random.randint(1, 4))
#     print(os.getpid(), 'end')
#
# # 先开4个进程，其中有进程结束时会有新的进程进去，始终使用开启的4个进程
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(4)    # 在该进程池中开4个进程程
#     for i in range(10):
#         tp.submit(func, i, i+1)    # (传递参数) 把任务提交给池，池替你执行进程中的任务



# 获取任务结果：
# import time
# import random
# import os
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
# def func(a, b):
#     print(os.getpid(), 'start', a, b)
#     time.sleep(random.randint(1, 4))
#     print(os.getpid(), 'end')
#     return a * b
#
#
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(4)
#     future_l = {}
#     for i in range(10):    # 异步非阻塞
#         ret = tp.submit(func, i, i+1)
#         # print(ret.result())    # Future对象（现在放进去，未来才用到）
#         future_l[i] = ret
#     for key in future_l:    # 这里获取结果时同步的
#         print(key, future_l[key].result())


# map  tp对象的map 只适合传递简单的参数，并且必须是一个可迭代的类型作为参数
# import time
# import random
# import os
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
#
# def func(a):
#     b = a + 1
#     print(os.getpid(), 'start', a, b)
#     time.sleep(random.randint(1, 4))
#     print(os.getpid(), 'end')
#     return a * b
#
#
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(4)
#     ret = tp.map(func, range(20))
#     for key in ret:
#         print(key)


# 回调函数： 效率最高
import time
import random
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor

def func(a, b):
    # print(current_thread().ident, 'start', a, b)
    time.sleep(random.randint(1, 4))
    # print(current_thread().ident, 'end')
    return (a, a * b)
def print_func(ret):    # 回调过程 异步阻塞
    print(ret.result())

if __name__ == '__main__':
    tp = ThreadPoolExecutor(4)
    future_l = {}
    for i in range(20):    # 异步非阻塞的
        ret = tp.submit(func, i, i+1)
        # ret这个任务会在执行完毕的瞬间立即触发print_func函数，并且把任务的返回值对象传递到print_func做参数
        ret.add_done_callback(print_func)    # 异步阻塞
        # 异步阻塞 回调函数 给ret对象绑定一个回调函数，等待ret对应的任务有了结果之后立即调用print_func这个函数
        # 就可以对结果立即进行处理，而不用按照顺序接受结果处理结果