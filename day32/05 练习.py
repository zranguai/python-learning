# 练习1：multiprocess模块
# from multiprocessing import Process
# import time
#
# def func(a, b):
#     time.sleep(1)
#     print('in func')
#     print(a, b)
#
# def foo():
#     print('in foo')
# if __name__ == '__main__':
#     p1 = Process(target=func, args=(1, 2))    # 可以传递参数(参数形式为元组)
#     p2 = Process(target=foo)
#     p1.start()    # 开启进程
#     print('in main first')
#     p1.join()    # 等待p1结束
#     p2.start()
#     p2.join()
#     print('in main end')

# 练习2：进程之间数据是否隔离？
from multiprocessing import Process
n = 0
def func():
    global n
    n += 1
    print(n)

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=func)
        p.start()
    print('in main', n)
















