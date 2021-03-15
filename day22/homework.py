# 作业1
# 是有序列表
# 二分查找[1,2,3,4,5,6,7,8,9,10,27,36,46,58,69]
# 1.递归做
import math
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 27, 36, 46, 58, 69]
# lst = [1, 3, 5, 7, 9, 10, 25, 36]
# def search_value(value, start = 0, end = len(lst)):
#     mid = math.floor((end - start) / 2)
#     if lst[mid] > value:
#         end = mid - 1
#         return search_value(value, end)
#     elif lst[mid] < value:
#         start = mid + 1
#         return search_value(value, start)
#     else:
#         return mid
#
# ret = search_value(10)
# print(ret)
# 2.循环做（不推荐）
# 作业2
# shutil.copy2('原文件','现文件')
# sys.argv练习
# 写一个python脚本，在cmd里执行
# python xxx.py 用户名 密码 cp(拷贝)    文件路径  目的地址
# 例如：python xxx,py alex sb cp 文件路径  目的地址  [五个参数]
# import sys
# import shutil
#
# username = sys.argv[1]
# password = sys.argv[2]
#
# path1 = sys.argv[3]
# path2 = sys.argv[4]
# # cp = sys.argv[5]()
#
# def cp(path1, path2):
#     shutil.copytree(path1, path2)
#
# while username == 'alex' and password == '123':
#     cp(path1, path2)
#     break
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




# 作业3：使用walk来计算文件夹的总大小
# os模块中的walk
import os
g = os.walk('D:\老男孩python22期代码及笔记\day21')
# for i in g:
#     print(i)
size = 0
for i in g:
    path, dir_list, name_list = i
    for j in name_list:
        path_detail = os.path.join(path, j)
        print(path_detail)
        size += os.path.getsize(path_detail)
    print(path)
print(size)

# 练习题2
# 定义一个圆形类，半径是这个圆形的属性，实例化一个半径为5的圆形，一个半径为10的圆形
# 完成方法：计算圆的面积，计算园的周长
# class Circle:
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         return self.r * self.r * 3.14
#     def perimeter(self):
#         return round(2 * 3.14 * self.r, 2)
#
# r5 = Circle(5)
# r10 = Circle(10)
# # print(r5.r)
# # print(r10.r)
# print(r5.area())
# print(r5.perimeter())


# 定义一个用户类，用户名和密码是这个类的属性，实例化两个用户，分别有不同的用户名和密码
# 完成方法：
# 登入成功后才创建用户对象
# 设计一个方法 修改密码
# （之前密码，修改后密码）
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#     def change_pwd(self, newpwd):
#         self.password = newpwd
#
#
# xiaoming = User('小明', 123)
# xiaohong = User('小红', 456)
# print(xiaohong.username)
# print(xiaohong.password)
# xiaohong.change_pwd(789)
# print(xiaohong.password)



# 选择做
# 继续完成人狗大战
# 你是人
# 狗是一个npc
# 你一个回合，狗一个回合
# 狗掉的血是一个波动值
# 闪避概率

# 继续完成计算器