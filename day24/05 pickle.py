# 将对象利用pickle存储在文件中
# pickle可以连续的drump进去/连续load出来
class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

python = Course('python','6个月', 21800)
linux = Course('linux','5个月', 18800)
go = Course('go','4个月', 11800)
import pickle
# with open('pickle_file', 'ab') as f:
#     # pickle.dump(python, f)
#     pickle.dump(linux, f)
#     pickle.dump(go, f)

with open('pickle_file', mode='rb') as f1:
    while True:
        try:
            obj = pickle.load(f1)
            print(obj.name, obj.period)
        except EOFError:
            break





















