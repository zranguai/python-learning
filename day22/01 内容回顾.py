# 作业1
# 二分查找[1,2,3,4,5,6,7,8,9,10,27,36,46,58,69]
# 1.递归做
# 2.循环做（不推荐）
# 作业2
# sys.argv练习
# 写一个python脚本，在cmd里执行
# python xxx.py 用户名 密码 cp(拷贝)    文件路径  目的地址
# 例如：python xxx,py alex sb cp 文件路径  目的地址  [五个参数]

# 作业3：使用walk来计算文件夹的总大小
# os模块中的walk
import os
g = os.walk('D:\老男孩python22期代码及笔记\day21')
# for i in g:
#     print(i)
for i in g:
    path, dir_list, name_list = i
    print(path, name_list)














