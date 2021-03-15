#
# 1.整理函数相关知识点,写博客。
#
# 2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def odd_element(li):
#     l1 = li[1::2]
#     return l1
#
#
# l2 = [1, 2, 3, 6, 5, 8]
# tu2 = (1, 2, 3, 6, 5, 8)
# res = odd_element(l2)
# res1 = odd_element(tu2)
# print(res)
# print(res1)
# 3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def judge_length(li):
#     if len(li) > 5:
#         return True
#     else:
#         return False
#
#
# print(judge_length('askdhajdaj'))
# print(judge_length([1, 2, 3, 5]))
# print(judge_length((1, 2, 3, 5, 6, 9)))
# 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def check_length(li):
#     return li[0:2] if len(li) > 2 else False
#
#
# print(check_length([1, 2, 3, 6, 8]))
# print(check_length([18]))
# 5.写函数，计算传入函数的字符串中,[数字]、[字母] 以及 [其他]的个数，并返回结果。
# s1 = '256aasdf582中文学习'
# i.isalpha不能判断中英文
# def foo(s):
#     num1 = 0
#     s1 = 0
#     other = 0
#     for i in s:
#         if i.isdigit():
#             num1 += 1
#         elif i.encode('utf-8').isalpha():
#             s1 += 1
#         else:
#             other += 1
#     return num1, s1, other
#
#
# res = foo('256aasdf582中文k学习')
# print(res)
# 6.写函数，接收两个数字参数，返回比较大的那个数字。
# def foo(num1, num2):
#     return num1 if num1 > num2 else num2
#
#
# print(foo(53, 23))
# print(foo(0, 23))
# 7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}    {"k1": "v1", "k2": [11,22]}
# PS:字典中的value只能是字符串或列表
# dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
# def foo(dic):
#     dic1 = {}
#     for i in dic.keys():
#         if len(dic[i]) > 2:
#             dic1[i] = dic[i][0:2]
#     return dic1
#
#
# print(foo(dic))
# 8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
# 此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# l1 = [11, 22, 33, 44, 25]
# def foo(l1):
#     dic = {}
#     for index in range(len(l1)):
#         dic[index] = l1[index]
#     return dic
#
#
# print(foo(l1))
# 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。
# 用户通过输入这四个内容，然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
# def foo(name, sex, age, edu):
#     s1 = '姓名是：{}，性别是：{}，年龄是：{}，学历是：{}\n'.format(name, sex, age, edu)
#     with open('student_msg', mode='a', encoding='utf-8') as f:
#         f.write(s1)
#
#
# foo('小明', '男', 23, '本科')
# foo('小红', '女', 21, '专科')
# 10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
# 用户持续输入： while input
# # 函数：接收四个参数。将四个参数追加到文件中。
# def foo(name, age, edu, sex='男'):
#     s1 = '姓名是：{}，性别是：{}，年龄是：{}，学历是：{}\n'.format(name, sex, age, edu)
#     with open('student_msg', mode='a', encoding='utf-8') as f:
#         f.write(s1)
#
#
# while True:
#     if input('输入q/Q退出,输入其他继续').upper() == 'Q':
#         break
#     name = input('请输入姓名')
#     sex = input('请输入性别')
#     age = input('请输入年龄')
#     edu = input('请输入学历')
#     foo(name, age, edu, sex)
# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（选做题）。
#
# import os
# def foo(name, change):
#     with open(name, mode='r', encoding='utf-8') as f1, \
#             open(name + '.bak', mode='w', encoding='utf-8') as f2:
#         old_content = f1.read()
#         new_content = old_content.replace('SB', change)
#         f2.write(new_content)
#     os.remove(name)
#     os.rename(name + '.bak', name)
#
# foo('student_msg', 'alexxx')