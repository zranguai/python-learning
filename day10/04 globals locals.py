""""
本文研究globals/locals
"""
a = 1
b = 2
def func():
    name = 'alex'
    age = 73
    print(globals())  # 返回的是字典：字典里面的键值对：全局作用域的所有内容
    print(locals())   # 返回的是字典：字典里面的键值对，当前作用域的所有内容


# print(globals())    # 返回的是字典：字典里面的键值对：全局作用域的所有内容
# print(locals())     # 返回的是字典：字典里面的键值对，当前作用域的所有内容
func()


# 今日总结：
# 1.参数：万能参数，仅限关键字参数（了解），参数的顺序，*的魔性用法：聚合，打散
# 2.名称空间，作用域，取值顺序，加载顺序，
# 3.高阶函数：执行顺序
# 4.globals locals
# 明天下午考试
