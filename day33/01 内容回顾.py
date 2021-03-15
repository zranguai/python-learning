# 概念
    # 同步异步阻塞和非阻塞
        # 同步阻塞 : 调用一个函数需要等待这个函数的执行结果,并且在执行这个函数的过程中CPU不工作
            # inp = input('>>>')
        # 同步非阻塞 :调用一个函数需要等待这个函数的执行结果,在执行这个函数的过程中CPU工作
            # ret = eval('1+2+3-4')
        # 异步非阻塞 :调用一个函数不需要等待这个函数的执行结果,并且在执行这个函数的过程中CPU工作
            # start()
        # 异步阻塞 : 调用一个函数不需要等待这个函数的执行结果,并且在执行这个函数的过程中CPU不工作
            # 开启10个进程 异步的
            # 获取这个进程的返回值,并且能做到哪一个进程先结束,就先获取谁的返回值
    # 进程的三状态图
        # 就绪 -操作系统调度->运行 -遇到io操作-> 阻塞 -阻塞状态结束-> 就绪
        #                         -时间片到了-> 就绪
    # 进程的调度算法 : 短作业和长作业是有区别的,越长的作业被调度的没有短作业调度的积极
                     # 每一个io操作都会让你辛苦排来的队执行的CPU机会让给其他程序
        # 先来先服务
        # 短作业优先
        # 分时的概念
        # 多级反馈算法
    # 进程开启和关闭
        # 父进程 开启了 子进程
        # 父进程 要负责给 子进程 回收子进程结束之后的资源

from multiprocessing import Process
import time
def task(m):
    print(123)
    print(345)
    print(f'执行了{m}')
    time.sleep(1)

def task1(n):
    print('haha')
    print(n)
if __name__ == '__main__':
    p1 = Process(target=task, args=('p1', ))

    p2 = Process(target=task, args=('p2', ))
    p1.start()
    p2.start()
    p1.join()   # 阻塞 等待p1执行完毕 join:加入
    p2.join()   # 阻塞 等待P2执行完毕
    p3 = Process(target=task1, args=(25,))
    p3.start()






















