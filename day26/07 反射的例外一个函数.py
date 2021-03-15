# hasattr()   一般和getattr在一起
# callable()  判断是否能够调用
class Person:
    def __init__(self, name):
        self.name = name
    def func(self):
        print('haha')

# a = Person('haha')
# print(hasattr(a, 'name'))
# print(hasattr(a, 'age'))
# print(hasattr(a, 'sex'))

if hasattr(a, 'func'):
    if callable(getattr(a, 'func')):
        getattr(a, 'func')()

# print(callable(a.func))
# print(callable(a.haha))
























