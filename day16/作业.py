# 2.写函数：用户输入某年某月，判断这是这一年的第几天（需要用Python的结构化时间）。 结构化时间可以通过这样取值：
#
# import time
# year, month = input("year:"), input("month:")
# print(time.strptime(f"{year}-{month}-1 13:22:22", "%Y-%m-%d %H:%M:%S").tm_yday)
# 3.用户输入一个"2019-7-26 20:30:30"和当前时间相比,一共过去了多少年多少月多少天到少小时多少分钟
#
# import time
# time1 = "2019-7-26 20:30:30"
# old = time.mktime(time.strptime(f'{time1}', '%Y-%m-%d %H:%M:%S'))
# now = time.mktime(time.localtime())
# chazi = abs(now - old)
# if now > old:
#     loc = time.localtime(chazi)
#     o = time.localtime(0)
#     print(loc)
#     print(f"一共过去了{loc.tm_year - o.tm_year}年{loc.tm_mon - o.tm_mon}月{loc.tm_mday- o.tm_mday}天"
#           f"{loc.tm_hour - o.tm_hour}时{loc.tm_min-o.tm_min}分{loc.tm_sec - o.tm_sec}秒")
# else:
#     loc = time.localtime(0)
#     o = time.localtime(chazi)
#     print(loc)
#     print(f"还差{loc.tm_year - o.tm_year}年{loc.tm_mon - o.tm_mon}月{loc.tm_mday- o.tm_mday}天"
#           f"{loc.tm_hour - o.tm_hour}时{loc.tm_min-o.tm_min}分{loc.tm_sec - o.tm_sec}秒")
#
# print(chazi)
# 4.写函数，生成一个4位随机验证码（包含数字大小写字母)
import random
# s1 = str(chr(random.randint(97, 122)))
# print(chr(random.randint(97, 122)))
# print(s1)
# def ran():
#     a = str(random.randint(0, 9))
#     + str(chr(random.randint(97, 122)))
#     + str(chr(random.randint(65, 90)))
#     + str(chr(random.randint(65, 90)))
#     lst = a.split()
#     random.shuffle(lst)
#     s = ""
#     for i in lst:
#         s = s + i
#     print(s)
#
# ran()

def ran():
    lst = []
    lst.append(str(random.randint(0, 9)))
    lst.append(chr(random.randint(97, 122)))
    lst.append(chr(random.randint(65, 90)))
    lst.append(chr(random.randint(65, 90)))
    random.shuffle(lst)
    s = ""
    for i in lst:
        s += i
    print(s)

ran()