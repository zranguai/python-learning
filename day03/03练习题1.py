# 有字符串s = '123a4b5c'
s = '123a4b5c'
# a.通过对s切片形成新的字符串s1 = '123'
# s1 = s[0:3]
# print(s1)
# a.通过对s切片形成新的字符串s2 = 'a4b'
# s2 = s[3:6]
# print(s2)
# a.通过对s切片形成新的字符串s3 = '1345'
# s3 = s[0::2]
# print(s3)
# a.通过对s切片形成新的字符串s4 = '2ab'
# s4 = s[1:-2:2]
# print(s4)
# a.通过对s切片形成新的字符串s5 = 'c'
# s5 = s[-1:-2:-1]
# print(s5)
# a.通过对s切片形成新的字符串s6 = 'ba2'
# s6 = s[-3:0:-2]
# print(s6)


# 字符串常用操作方法  (中文忽略)

# 不会对原来字符串产生新的操作，都是产生一个新的字符串
# s = 'tAiBai'
# s1 = s.upper()
# print(s1)
# s2 = s.lower()
# print(s2)

# 应用
# username = input('请输入用户名')
# password = int(input('请输入密码'))
# code = 'qwEa'
# your_code = input('请输入验证码')
# if code.upper() == your_code.upper():
#     if username == 'haha' and password == 123:
#         print('成功')
#     else:
#         print('用户名或密码错误')
# else:
#     print('验证码错误')

# s = 'tAiBai'
# print(s.startswith('tA'))
# print(s.startswith('tAi'))
# 了解
# print(s.startswith('i', 2, 5))

# replace
# msg = 'gg不是mm, mm不是gg'
# msg1 = msg.replace('gg', 'xx', 1)
# print(msg1)

# strip: 空格/空白，\t(空格) \n(换行)    只能去除左右两边的
# s4 = '  \n哈哈     哈hehe\t  '
# s5 = s4.strip()
# print(s5)
# 了解：可以去除指定字符
# s4 = 'rre哈哈哈qqd'
# s5 = s4.strip('red')
# print(s5)

# split  非常重要
# 默认按照空格分隔，返回一个列表
# str -----> list
# s6 = '哈哈哈 嘿嘿 呵呵呵'
# ll = s6.split()
# print(ll)
# 指定分隔符
# s7 = ',kk,ll,ss'
# l1 = s7.split(',')
# print(l1)
# print(s7.split(',', 2))

# join   list ----> str
# 前提：列表里面的元素必须是str类型
# l1 = ['哈哈', '呵呵', '黑金额']
# s2 = ':'.join(l1)
# print(s2)

# count: 数出某个字符串出现的次数
# s8 = 'ahashhsauwaaakkksaa'
# print(s8.count('a'))

# format:格式化输出
# 第一种用法
# msg = '我叫{}今年{}'.format('哈哈', 18)
# print(msg)
# 第二种用法：
# msg = '我叫{0}今年{1},也就是{0}'.format('哈哈', 18)
# print(msg)
# 第三种用法
# msg = '我叫{name},今年{age}'.format(age='55', name='哈哈')
# print(msg)

# is 系列
# name = 'hahaha123'
# age = '100'
# print(name.isalnum()) # 字符串由字母或者数字组成
# print(name.isalpha()) # 字符串由字母组成
# print(age.isdecimal()) # 字符串由十进制组成

# in 和 notin
s10 = 'aaabbbcccddd'
print('a' in s10)
print('cccc' in s10)
print('ee' not in s10)
print('bb' not in s10)