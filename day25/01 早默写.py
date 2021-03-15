# 1.内置的数据结构
# {}， [], (), {1,} 'haha'

# 11:30
# 非python内置的数据结构
# 1.Queue队列 先进先出
# put
# get
# class Queue:
#     def __init__(self, lst):
#         self.lst = lst
#     def put(self, value):
#         self.lst.append(value)
#     def get(self):
#         return self.lst.pop(0)
# queue = Queue([])
# queue.put(2)
# queue.put(5)
# queue.put(6)
# queue.put(4)
# print(queue.lst)
# ret = queue.get()
# print(ret)
# print(queue.lst)
# 2.Stack栈  后进先出
# put
# get
# class Stack:
#     def __init__(self, lst):
#         self.lst = lst
#     def put(self, value):
#         self.lst.append(value)
#     def get(self):
#         return self.lst.pop(len(self.lst) - 1)
# stack = Stack([])
# stack.put(2)
# stack.put(5)
# stack.put(6)
# stack.put(4)
# print(stack.lst)
# ret = stack.get()
# res = stack.get()
# print(ret)
# print(res)
# print(stack.lst)

# 3.继承关系
# 完成代码的简化
class Chun:
    def __init__(self, lst):
        self.lst = lst
    def put(self, value):
        self.lst.append(value)
class Queue(Chun):
    def get(self):
        return self.lst.pop(len(self.lst) - 1)
class Stack(Chun):
    def get(self):
            return self.lst.pop(len(self.lst) - 1)
# queue = Queue([])
# queue.put(2)
# queue.put(5)
# queue.put(6)
# queue.put(4)
# print(queue.lst)
# ret = queue.get()
# print(ret)
# print(queue.lst)
# stack = Stack([])
# stack.put(2)
# stack.put(5)
# stack.put(6)
# stack.put(4)
# print(stack.lst)
# ret = stack.get()
# res = stack.get()
# print(ret)
# print(res)
# print(stack.lst)

# 自定义pickle(借助pickle模块来完成简化的drump和load)
# pickle dump
# 打开文件
# 把数据dump到文件中
# pickle load
# 打开文件
# 读数据

# 对象 = Mypickle('文件路径')
# 对象.load() 能拿到这个文件中的所有对象
# 对象.dump()(要写入文件的对象)
import pickle
class Mypickle:
    def __init__(self, path, name):
        self.path = path
        self.name = name
    def dump(self):
        with open(self.path, mode='ab') as f1:
            pickle.dump(self, f1)
    def load(self):
        with open(self.path, mode='rb') as f2:
            while True:
                try:
                    yield pickle.load(f2)
                except Exception:
                    break
mypickle = Mypickle('pppiic', '小白')
# mypickle.dump()
# mypickle.load()
# print(mypickle.name)

















