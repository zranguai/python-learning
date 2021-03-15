# 文件操作的读：r,rb,r +,r+b 四种模式(前两种常用)
# A: mode='r'（r模式可以省略）

# 1.read() 全读出来 **
# f1 = open('文件的读', mode='r', encoding='utf-8')
# content = f1.read()
# print(content, type(content))
# f1.close()

# 2.read(n) 按照字符读取
# f1 = open('文件的读', mode='r', encoding='utf-8')
# content = f1.read(4)
# print(content)
# f1.close()

# 3.readline(n) 按照行读取
# f1 = open('文件的读', mode='r', encoding='utf-8')
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# f1.close()

# 4.readlines() 返回一个列表，列表中的每个元素是源文件的每一行
# f1 = open('文件的读', mode='r', encoding='utf-8')
# l1 = f1.readlines()
# print(l1)
# for line in l1:
#     print(line)
# f1.close()

# 5.for循环读取 *** (f1在内存中只占一行，当访问下一行时，上一行消失)
# f1 = open('文件的读', mode='r', encoding='utf-8')
# for line in f1:
#     print(line)
# f1.close()


# B: mode='rb' :操作的是非文本的文件，图片，视频，音频
# rb模式打开不用encoding
# f = open('汽车.jpg', mode='rb')
# content = f.read()
# print(content)
# f.close()

