# python 提供了68个内置函数
# 今天今天讲的这部分了解即可
# all()  any()  bytes() callable() chr() complex() divmod()
# eval() exec() format() frozenset() globals() hash() help()
# id() input() int()  iter() locals() next()  oct()  ord()  pow()    repr()  round()
#

# [在项目中使用可能会带来一些病毒]（尤其是1.网络传输的str 2.input输入的时候 3.sql注入的时候等等绝对不能使用eval）
# 1.eval() ** 剥去字符串的外衣运算里面的代码,有返回值
# s1 = '1 + 3'
# print(s1)
# print(eval(s1), type(eval(s1)))

# s = '{"name": "alex"}'
# print(s, type(s))
# # print(dict(s))    # 不行的
# print(eval(s), type(eval(s)))

# 2.exec() 与eval()几乎一样 ，处理代码流
# msg = """
# for i in range(10):
#     print(i)
# """
# print(msg)
# exec(msg)

# 3.hash() 哈希值(获取一个对象（可哈希对象：int，str，Bool，tuple）的哈希值。)
# print(hash('shgduasua'))

# 4.help() ** 函数用于查看函数或模块用途的详细说明
# print(help(str))
# print(help(str.upper))

# 5.callable() ***  函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功
# s1 = 'jsashj'
# def func():
#     pass
# print(callable(s1))
# print(callable(func))

# 6.bin() ** 将十进制转换成二进制并返回
# print(bin(10), type(bin(10)))
# 7.oct() ** 将十进制转化成八进制字符串并返回
# print(oct(10), type(oct(10)))
# 8.hex() ** 将十进制转化成十六进制字符串并返回
# print(hex(10), type(hex(10)))
# 9.complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
# 如果第一个参数为字符串，则不需要指定第二个参数.
# print(complex(2, 3))
# 10.divmod() ** 计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)。
# print(divmod(10, 3))
# 11.round() ** 保留浮点数的小数位数，默认保留整数。
# print(round(3.1415926, 2))  # 3.14
# 12.pow() ** 求x**y次幂。（三个参数为x**y的结果对z取余）
# print(pow(2, 3))
# print(pow(2, 3, 3))
# 13.bytes() *** 用于不同编码之间的转化。
# s1 = '哈哈'
# 1. b = s1.encode('utf-8')
# print(b)
# 2. b = bytes(s1, encoding='utf-8')
# print(b)
# 14.ord() 输入字符找该字符编码的位置
# 没超过ascil码超过Unicode编码
# print(ord('a'))
# print(ord('中'))    # (Unicode编码)
# 15.chr（）输入位置数字找出其对应的字符（Unicode编码）
# print(chr(97))    # a
# print(chr(20013))    # 中    （Unicode编码）
# 16.repr（）返回一个对象的string形式（原形毕露）。***(面向对象会用到)
# s1 = '哈哈'
# print(repr(s1))
# msg = '我叫%s' %(s1)
# msg = '我叫%r' %(s1)
# print(msg)
# 17.all（）可迭代对象中，全都是True才是True
# l1 = [1, 2, '哈哈', '']
# print(all(l1))
# 18.any（）可迭代对象中，有一个True 就是True
l1 = [0, False, '哈哈', '']
print(any(l1))
# 今日总结
# 1.生成器 ***
# 2.生成器函数 yield
# 3.yield 与 return区别
# 4.列表推导式，生成器表达式。***
# 5.内置函数：今天讲的内置函数，了解

