# from threading import Thread
# 数据不安全例子
# n = 0
# def add():
#     for i in range(500000):
#         global n
#         n += 1
# def sub():
#     for i in range(500000):
#         global n
#         n -= 1
#
# t_l = []
# for i in range(2):
#     t1 = Thread(target=add)
#     t1.start()
#     t2 = Thread(target=sub)
#     t2.start()
#     t_l.append(t1)
#     t_l.append(t2)
# for t in t_l:
#     t.join()
# print(n)


# 线程安全例子
# from threading import Thread
# import time
# n = []
# def append():
#     for i in range(500000):
#         n.append(1)
# def pop():
#     for i in range(500000):
#         if not n:
#             time.sleep(0.0000001)
#         n.pop()
#
# t_l = []
# for i in range(20):
#     t1 = Thread(target=append)
#     t1.start()
#     t2 = Thread(target=pop)
#     t2.start()
#     t_l.append(t1)
#     t_l.append(t2)
# for t in t_l:
#     t.join()
# print(n)


# += -=  *= /= while if 数据不安全   + 和 赋值是分开的两个操作
# append pop strip数据安全 列表中的方法或者字典中的方法去操作全局变量的时候 数据安全的
# 线程之间也存在数据不安全

# import dis
# a = 0
# def func():
#     global a
#     a += 1
# dis.dis(func)
'''
 56           0 LOAD_GLOBAL              0 (a)
              2 LOAD_CONST               1 (1)
              4 INPLACE_ADD
              # GIL锁切换了
              6 STORE_GLOBAL             0 (a)
'''




# import dis
# a = []
# def func():
#     a.append(1)
#
# dis.dis(func)
'''
 70           0 LOAD_GLOBAL              0 (a)
              2 LOAD_ATTR                1 (append)
              4 LOAD_CONST               1 (1)
              6 CALL_FUNCTION            1
              8 POP_TOP
'''











