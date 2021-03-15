# dumps
# loads
# dump
# load

def func():
    print('in func')
import pickle
# f = open('pickle对象', mode='wb')
# pickle.dump(func, f)
# f.close()

f = open('pickle对象', mode='rb')
ret = pickle.load(f)
print(ret)
print(ret())
f.close()

