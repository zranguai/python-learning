# 练习题1
name = "aleX leNb"
# print(name)
# print(name.upper())
# print(name.lower())
# print(name.startswith('ale'))
# print(name.endswith('Nb'))
# print(name.replace('a', 'z'))
# print(name.replace('l', 'v', 1))
# print(name.split('l', 1))
# print(name[0:4])

# 练习题2
# s = "123a4b5c"
# print(s[-2])

# 练习题3 使用while和for循环分别打印字符串s="asdfer"中每个元素
s = "asdfer"
# i = 0
# while循环
# while i < len(s):
#     print(s[i])
#     i += 1
# for循环
# for i in s:
#     print(i)

# 练习题4 使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"~
# s="asdfer"
# for i in s:
#     print(s)

# 练习题5 使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# s = '321'
# for i in s:
#     s = '倒计时{}秒'.format(i)
#     print(s)
# print('出发')

# 练习题6 实现一个整数加法计算器(两个数相加)
# user = input('请输入1或q,1进入，q退出')
# while user != 'q':
#     content = input('请输入两个数相加，例如 3+2')
#     s1 = content.split('+')
#     print(int(s1[0]) + int(s1[1]))
#     user = input('请输入1或q,1进入，q退出')
# else:
#     print('退出成功')

# 练习题7 实现一个整数加法计算器（多个数相加）
# user = input('请输入1或q,1进入，q退出')
# sum1 = 0
# while user != 'q':
#     content = input('请输入多个数相加，例如 3+2')
#     s1 = content.split('+')
#     for i in s1:
#         sum1 += int(i)
#     print(sum1)
#     user = input('请输入1或q,1进入，q退出')
# else:
#     print('退出成功')

# 练习题8 计算用户输入的内容中有几个整数（以个位数为单位）
# user = input('请输入内容')
# sum2 = 0
# for i in user:
#     if i.isdecimal():
#         sum2 += 1
# print(sum2)
# 练习题9 计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
# i, sum1 = 1, 0
# while i < 100:
#     if i % 2 != 0:
#         sum1 += i
#     else:
#         sum1 -= i
#     i += 1
# print(sum1 + 88)
# 练习题10 公交车
content = '''
A:公交车/步行（M:公交车，N：步行）
B:走小路回家
C:绕道回家(去游戏厅X或者网吧Y)
'''
# print(content)
# while True:
#     choose = input('请做出你的选择A/B/C')
#     if choose == 'A':
#         a = input('请做出你的选择：M:公交车，N：步行')
#         if a == 'M':
#             print('显示10分钟到家')
#             break
#         else:
#             print('显示20分钟到家')
#             break
#     elif choose == 'B':
#         print('走小路回家')
#         break
#     else:
#         print('绕道回家')
#         b = input('去游戏厅X或者网吧Y')
#         if b == 'X':
#             print('一个半小时到家找爸')
#         elif b == 'Y':
#             print('两个小时回家找妈')

# 练习题11 判断回文
a = "十八到日本日到八十"
s10 = a[::-1]
if a == s10:
    print('是回文')
else:
    print('不是回文')
