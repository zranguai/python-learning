# path1 = D:\老男孩python22期代码及笔记\day21\haha
# path2 = D:\老男孩python22期代码及笔记\day22\cece
# 答案：
# python D:\python_22\day23\2.作业讲解_函数相关的.py alex sb move D:\python_22\day23\文件  D:\python_22\day24
# python D:\python_22\day23\2.作业讲解_函数相关的.py alex sb mkdir D:\python_22\新的文件夹名

# 9月8号作业，
# 在这个基础上实现一个remove 把一个文件或者文件夹移动到例外一个位置
# 创建一个文件夹mkdir()
import os
import sys
import shutil
if len(sys.argv) >= 5:
    if sys.argv[1] =='alex' and sys.argv[2] == 'sb':
        if sys.argv[3] == 'cp' and len(sys.argv) == 6:
            if os.path.exists(sys.argv[4]) and os.path.exists(sys.argv[5]):
                filename = os.path.basename(sys.argv[4])
                path = os.path.join(sys.argv[5], filename)
                shutil.copy2(sys.argv[4], path)
        elif sys.argv[3] == 'rm' and len(sys.argv) == 5:
            if os.path.exists(sys.argv[4]):
                if os.path.isfile(sys.argv[4]):os.remove(sys.argv[4])
                else:shutil.rmtree(sys.argv[4])
        elif sys.argv[3] == 'rename'and len(sys.argv) == 6:
            if os.path.exists(sys.argv[4]):
                    os.rename(sys.argv[4],sys.argv[5])
else:
    print('您输入的命令无效')