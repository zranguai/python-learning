# 练习1：threading模块
# 方式1
# from threading import Thread
# import time
#
# def func():
#     time.sleep(0.1)
#     print('in func')
#
# if __name__ == '__main__':
#     t1 = []
#     for i in range(10):
#         t = Thread(target=func)
#         t.start()
#         t1.append(t)
#
#     for j in t1:
#         j.join()
#
#     print('所有线程都结束了')

# 方式2：
# from threading import Thread
#
# class Myclass(Thread):
#     def run(self):
#         print('in run')
#
# if __name__ == '__main__':
#     mc = Myclass()
#
#     mc.start()

# 练习2：线程之间数据是共享的
# from threading import Thread
#
# n = 0
# def fun():
#     global n
#     n += 1
# for i in range(4):
#     t = Thread(target=fun)
#     t.start()
# print(n)



























