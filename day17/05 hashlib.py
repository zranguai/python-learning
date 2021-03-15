"""
    用法：将bytes类型的字节转换成固定长度的16进制数字组成的字符串
"""
import hashlib
# s1 = hashlib.md5()
# s1.update('ab1256c哈哈'.encode('utf-8'))
# res = s1.hexdigest()
# print(res)
# print(type(res))


# 加盐
# s2 = '12589'
# ret = hashlib.md5('太白太白'.encode('utf-8'))
# ret.update(s2.encode('utf-8'))
# print(ret.hexdigest())

# 动态的盐
# s2 = '12589'
# ret = hashlib.md5('太白太白'[::2].encode('utf-8'))
# ret.update(s2.encode('utf-8'))
# print(ret.hexdigest())

# sha系列


# 文件的校验
#
# linux中一切皆文件：文本文件，非文本文件，（音频，图像）
# 无论你下载的视频，还是软件（国外的软件）,往往都有一个md5值

