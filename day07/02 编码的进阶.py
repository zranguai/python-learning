# A:英文：
# str: 'hello'
#   内存中表现方式：Unicode
#   表现形式：'hello'
# bytes:
#  内存中表现方式：非Unicode
#   表现形式：b'hello'

# B:中文：
# str: '中国'
#   内存中表现方式：Unicode
#   表现形式：'中国'
# bytes:
#  内存中表现方式：非Unicode （utf-8）
#   表现形式：b'\xe4\xb8\xad\xe5\x9b\xbd'

# str --> bytes
# s1 = '中国'
# b1 = s1.encode('utf-8')    #encode()编码
# print(b1, type(b1))
# bytes --> str
# b1 = b'\xe4\xb8\xad\xe5\x9b\xbd'
# s2 = b1.decode('utf-8')    #decode()解码
# print(s2)

# gbk --> utf-8
# b1 = b'\xd6\xd0\xb9\xfa'
# s = b1.decode('gbk')
# print(s)
# b2 = s.encode('utf-8')
# print(b2)

# python3x str为例，模拟将一句话通过网络发送给对方
# content就是那句话
# content = input('>>>')
# print(content, type(content))
# # bytes #
# b = b'hello'
# print(b.upper())
# print(b, type(b))

# s1 = '中国'
# # b = b'中国'
# b = s1.encode('utf-8')
# print(b)

# 总结：
# 1.数据类型的补充： list(sort,reverse,列表的加，乘，循环问题)， dict(update,循环问题)
# 2.编码的进阶：
# 1.bytes为什么存在？
# 2.str --> bytes(Unicode-->非Unicode)
# 3.gbk <--> utf-8(因为有的公司可能还是用python2,python2的编码是可能是gbk)
