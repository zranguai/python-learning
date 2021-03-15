# callable(对象)
# 能不能对象（）调用就看这个类有没有实现__call__方法
class A:
    def __call__(self, *args, **kwargs):
        print('-----------')

obj = A()
print(callable(obj))
obj()
# Flask框架的源码































