# tell（）获取光标的位置 单位：字节
# f = open('文件的读写', encoding='utf-8')
# print(f.tell())
# content = f.read()
# print(f.tell())
# f.close()

# seek（n） 调整光标位置 单位：字节
# f = open('文件的读写', encoding='utf-8')
# print(f.seek(7))
# print(f.tell())
# content = f.read()
# print(f.tell())
# print(content)
# f.close()

# 应用：网络并发时的断点续传

# flush() 强制刷新(相当于ctrl + s保存文件)
f = open('文件的其他功能', mode='w', encoding='utf-8')
f.write('ajsdgasczbsdhags')
f.flush()
f.close()


