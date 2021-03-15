# 优点1：不用手动关闭文件句柄
# with open('文件的读', encoding='utf-8') as f:
#     print(f.read())

# 优点2：一个位置操作多个open(\换行)
with open('文件的读', encoding='utf-8') as f1, \
        open('文件的写', encoding='utf-8', mode='w') as f2:
    print(f1.read())
    f2.write('2455hashduay')


# 缺点：待续
