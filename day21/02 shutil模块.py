# 一般在手动压缩文件时推荐使用


import shutil

# 1.copy文件
# shutil.copy2('原文件', '现文件')
# shutil.copy2('D:\老男孩python22期代码及笔记\day20\lianjia.html', 'D:\老男孩python22期代码及笔记\day21\lianjia_bk.html')

# 2.copy目录
# shutil.copytree("原目录", "新目录")  # , ignore=shutil.ignore_patterns("*.pyc")) #[忽略什么文件不想copy]
# shutil.copytree("D:\老男孩python22期代码及笔记\day20\haha", "D:\老男孩python22期代码及笔记\day21\haha1", ignore=shutil.ignore_patterns("01 测测.py"))

# 3.rmtree()删除文件
# shutil.rmtree('文件', ignore_errors=True)   # ignore_errors忽略错误

# 4.move()移动 copy过来并把之前的删除掉
# shutil.move('原文件', '现文件', copy_function=shutil.copy2)

# 5.shutil.disk_usage() 查看当前磁盘使用空间
# total, used, free = shutil.disk_usage(".")  # .查看当前所在磁盘
# print(f'当前磁盘共：{total/1073741824}GB,已使用{used/1073741824}GB,剩余{free/1073741824}GB')

# 6.shutil.mark_archive()压缩文件
# shutil.make_archive('haha_z', 'zip', 'D:\老男孩python22期代码及笔记\day21\haha')

# 7.shutil.unpack_archive()解压文件
#     shutil.unpack_archive('haha_z.zip')
#     shutil.unpack_archive('haha_z.zip', r'D:\老男孩python22期代码及笔记\day21\测试')







