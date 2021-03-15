# import queue    # 线程之间数据安全的容器队列
# from queue import Empty    # 不是内置的错误类型，而是queue模块中的错误
#
# q = queue.Queue(4)    # fifo 先进先出队列
# # q.get()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# print('4 done')
#
# # q.put(5)
# # print('5 done')
# try:
#     q.get_nowait()
# except Empty:
#     pass
# print('队列为空，继续其他内容')



# from queue import LifoQueue    # last in first out 后进先出  栈
# lq = LifoQueue()
# lq.put(1)
# lq.put(2)
# lq.put(3)
# print(lq.get())
# print(lq.get())
# print(lq.get())


from queue import PriorityQueue    # 优先级队列

priq = PriorityQueue()
priq.put((2, 'alex'))
priq.put((1, 'wusir'))
priq.put((3, '太白'))

print(priq.get())
print(priq.get())
print(priq.get())











