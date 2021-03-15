"""
1. 以读的模式打开原文件
2. 以写的模式创建一个新的文件
3. 将原文件的内容读出来修改成新内容，写入新的文件
4. 将原文件删除
5. 将新文件重命名成原文件
"""
# low版本
# import os
# with open('alex自述', encoding='utf-8') as f1, \
#      open('alex自述.bak', mode='w', encoding='utf-8') as f2:
#     old_content = f1.read()
#     new_content = old_content.replace('alex', 'SB')
#     f2.write(new_content)
# os.remove('alex自述')
# os.rename('alex自述.bak', 'alex自述')

# 进阶版：
# import os
# with open('alex自述', encoding='utf-8') as f1, \
#      open('alex自述.bak', mode='w', encoding='utf-8') as f2:
#     for line in f1:
#         new_line = line.replace('SB', 'alex')
#         f2.write(new_line)
# os.remove('alex自述')
# os.rename('alex自述.bak', 'alex自述')


# 有关清空的问题 (只要文件没有关闭就会一直写入)
# 关闭文件句柄，再次以w模式打开此文件时才会清空
# with open('文件的写', mode='w', encoding='utf-8') as f1:
#     f1.write('lllllllllllll\n')
#     f1.write('lllllllllllll')
#     f1.write('lllllllllllll')
#     f1.write('lllllllldlllll')

# 今日总结：
#   文件操作： r(常用) w rb r+ ab
#             read() write() tell() seek() flush()
#             文件的改必须会