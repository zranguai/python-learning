# 文件的登入 上传 下载
# 1.看懂代码
# 2.根据代码把上传功能加上
# 3.把代码实现一个socketserver的版本

# 操作系统的历史
    # 多道操作系统
        # 遇到IO操作就切换的
        # 提高CPU的利用率
        # 进程之间数据隔离
        # 时空复用 : 再同一个时间点上,多个程序同时执行着,一块儿内存条上存储了多个进程的数据
    # 分时操纵系统
        # 时间分片
        # 时间片轮转
# 进程
    # 是计算机中最小的资源分配单位 : 每一个程序在运行起来的时候需要给分配一些内存
    # 一个运行的程序
    # 在操作系统中用pid来唯一标识一个进程
# 线程
    # 是计算机中能被CPU调度的最小单位 : 实际执行具体编译解释之后的代码的是线程,所以cpu执行的是解释之后的线程中的代码
# 并行和并发
    # 并发    : 一个CPU,多个程序轮流执行
    # 并行(好):多个cpu,各自在自己的cpu上执行多个程序
# 同步和异步
    # 同步 : 调用一个操作,要等待结果
    # 异步 : 调用一个操作,不等待结果
# 阻塞和非阻塞
    # 阻塞   : CPU不工作
    # 非阻塞 : CPU工作
# 同步阻塞
    # input sleep recv recvfrom
# 同步非阻塞
    # ret = eval('1+2+3+4+5')
# def func(*args):
#     count = 0
#     for i in args:
#         count += i
#     return count
# a = 1
# b = 2
# c = a + b
# d = func(a,b,c)
# print(d)

# 异步非阻塞(阻塞 blocking)
# 异步阻塞

# import socket
# sk =socket.socket()
# sk.setblocking(False)
# sk.bind(('127.0.0.1',9001))
# sk.listen()
#
# while True:
#     try:
#         conn,addr = sk.accept()
#     except BlockingIOError:
#         pass





