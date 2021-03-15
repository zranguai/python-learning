# 用字符串数据类型的名字 来操作这个名字对应的函数\实例变量\绑定方法\各种方法

# name = 'alex'
# age = 123
#
# n = input('>>>')
# if n == 'name':print(name)
# elif n == 'age':print(age)

# 有些时候 你明明知道一个变量的字符串数据类型的名字,你想直接调用它,但是调不到#
# 使用反射

# 1.反射对象的 实例变量
# 2.反射类的 静态变量/绑定方法/其他方法
# 3.模块中的 所有变量
#     被导入的模块
#     当前执行的py文件 - 脚本


# 对象名.属性名 ===> getattr(对象名, '属性名')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def qqxing(self):
        print('qqxinggggggg')

# alex = Person('alex', 83)
# wusir = Person('wusir', 74)
# ret = getattr(alex, 'name')
# print(ret)
# res = getattr(wusir, 'name')
# print(res)
# ret = getattr(wusir, 'qqxing')
# print(ret)
# ret()
# print(ret, wusir.qqxing)
# 调用函数：函数地址（）

# 反射其他模块的内容
import a
import sys
print(sys.modules['a'], Alipay)
print(a, Alipay)    # a为内存地址

# 反射本模块的内容
import sys
whaha = 'hahaha'
print(getattr(sys.modules['__main__'], 'whaha'))





























