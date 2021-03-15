# multiprocessing 多一案的处理进程的模块

#  类的名字用大写开头，文件的名字用小写开头
# from multiprocessing import Process
#
# import os
# import time
# def func(name, age):
#     print(f'{name}start')
#     time.sleep(1)
#     print(os.getpid(), os.getppid(), name, age)    # pid(进程id):process id ppid(父进程id):parent process id
# # print('123')
# if __name__ == '__main__':
#     # 只会在主进程中执行的所有的代码写在name = main下
#     print('main:', os.getpid(), os.getppid())
#     arg_lst = [('alex', 84), ('taibai', 73), ('wusir', 96)]
#     for arg in arg_lst:
#         p = Process(target=func, args=arg)    # 可以给子进程传递参数
#         p.start()  # 开启子进程,异步非阻塞
#     # p = Process(target=func, args=('haha', 23))    # 可以开启多个子进程
#     # p.start()


# 为什么要用if __name__ == '__main__'？
# 能不能给子进程传递参数？ 能
# 能不能获取子进程的返回值？不能
# 能不能同时开启多个子进程？可以
# join的用法
# from multiprocessing import Process
# import os
# import time
# def func(name, age):
#     print(f'发送一封邮件给{age}的{name}')
#     time.sleep(1)
#     print('发送完毕')
# if __name__ == "__main__":
#     arg_lst = [('alex', 84), ('taibai', 73), ('wusir', 96)]
#     p_lst = []
#     for arg in arg_lst:
#         p = Process(target=func, args=arg)
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:
#         p.join()    # 阻塞：直到p这个进程执行完毕才继续执行代码
#     print('所有邮件已经发送完毕')    # 要求：这句话最后打印，并且要求上面的能够异步执行
# 同步阻塞 异步非阻塞
# 同步阻塞：join()
# 异步非阻塞：start()

# 多进程之间的数据是否隔离
# from multiprocessing import Process
# n = 0
# def func():
#     global n
#     n += 1
#
# if __name__ == '__main__':
#     p_l = []
#     for i in range(50):
#         p = Process(target=func)
#         p.start()
#         p_l.append(p)
#     for p in p_l:
#         p.join()
#     print(n)    # 0 对主进程进行了隔离

# 使用多进程实现一个并发的soket的server








