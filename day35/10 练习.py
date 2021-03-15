# 练习1：守护线程
# from threading import Thread
# import time
# def son1():
#     while True:
#         print('in son1')
#         time.sleep(1)
#
# def son2():
#     for i in range(3):
#         print('in son2')
#         time.sleep(0.5)
#
# t = Thread(target=son1)
# t.daemon = True    # 会守护其他线程
# t.start()
# t1 = Thread(target=son2).start()

# 练习2：