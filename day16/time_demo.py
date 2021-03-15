# 今日学习模块 time/datetime/os/sys/hashlib/json/pickle/collections
"""1
    time模块
    三大对象：时间戳 结构化时间对象（9大字段）字符串
"""

import time
# 获取时间戳
# 时间戳：从时间元年（1970 1 1 00：00：00）到现在经过的秒数
# print(time.time())    # 1598673660.9252436

# 获取格式化时间对象(时间戳-->转换成格式化时间对象)：是九个字段组成的
# 默认是当前系统时间的时间戳
# print(time.gmtime())    # GMT格林尼治时间
# print(time.gmtime(1))    # 时间元年过一秒后的时间
# print(time.localtime())    # 当地时间

# 格式化时间对象-->转换成时间戳（time.mktime()）
# t1 = time.localtime()
# print(time.mktime(t1))

# 格式化时间对象--->字符串(time.strftime(format, t))
# s = time.strftime("year:%Y %m %d %H:%M:%S", )

# print(s)
# 把时间字符串--->格式化时间对象time.strptime(String, format)
# time_obj = time.strptime("2010 10 12", "%Y %m %d")
# print(time_obj)

# 暂停当前线程（程序），睡眠xxx秒
# time.sleep(1)
# print('哈哈')
# for i in range(5):
#     print(time.strftime("%Y-%m-%d %H:%M:%S"))
#     time.sleep(1)


