# 理解代码扩展性（不能写死）

# 有如下文件，a1.txt，里面的内容为：
# 老男孩是最好的学校，
#
# 全心全意为学生服务，
#
# 只为学生未来，不为牟利。
#
# 我说的都是真的。哈哈
#
# ​
#
# ​	分别完成以下的功能：
#
# ​	a.将原文件全部读出来并打印。
# f1 = open('a1', mode='r', encoding='utf-8')
# content = f1.read()
# print(content)
# f1.close()
# ​	b,在原文件后面追加一行内容：信不信由你，反正我信了。
# f1 = open('a1', mode='a', encoding='utf-8')
# f1.write('信不信由你，反正我信了。')
# f1.close()
# ​	c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
# f1 = open('a1', mode='r+', encoding='utf-8')
# content = f1.read()
# print(content)
# f1.write('信不信由你，反正我信了')
# f1.close()
# ​	d,将原文件全部清空，换成下面的内容：
#
# ​	每天坚持一点，
#
# ​	每天努力一点，
#
# ​	每天多思考一点，
#
# ​	慢慢你会发现，
#
# ​	你的进步越来越大。
# f1 = open('a1', mode='w', encoding='utf-8')
# f1.write('每天坚持一点/n每天努力一点/n每天多思考一点/n慢慢你会发现/n你的进步越来越大')
# f1.close()
# 2.有如下文件，t1.txt,里面的内容为：
#
# 葫芦娃，葫芦娃，
#
# 一根藤上七个瓜
#
# 风吹雨打，都不怕，
#
# 啦啦啦啦。
#
# 我可以算命，而且算的特别准:
#
# 上面的内容你肯定是心里默唱出来的，对不对？哈哈
#
# ​	分别完成下面的功能：
#
# ​	a,以r的模式打开原文件，利用for循环遍历文件句柄。
# f = open('t1', mode='r', encoding='utf-8')
# for line in f:
#     print(line)
# f.close()
# ​	b,以r的模式打开原文件，以readlines()方法读取出来，并循环遍历 readlines(),并分析a与b有什么区别？深入理解文件句柄与 readlines()结果的区别。
# f = open('t1', mode='r', encoding='utf-8')
# content = f.readlines()
# for line in content:
#     print(line)
# f.close()
# 区别： a一下读文件的一行 b.读列表的一项
# ​	c,以r模式读取‘葫芦娃，’前四个字符。
# f = open('t1', mode='r', encoding='utf-8')
# content = f.read(4)
# print(content)
# f.close()
# ​	d,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
# f = open('t1', mode='r', encoding='utf-8')
# content = f.readline()
# new_content = content.strip()
# print(content)
# print(new_content)
# f.close()
# ​	e,以a+ 模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将原内容全部读取出来。
# with open('t1', mode='a+', encoding='utf-8') as f:
#     f.write('老男孩教育')
#     f.seek(0)
#     print(f.tell())
#     print(f.read(5))
# 文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
# apple 10 3
#
# tesla 100000 1
#
# mac 3000 2
#
# lenovo 30000 3
#
# chicken 10 3
#
# ​	通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
#[{'name':'apple','price':10,'amount':3,'year': 2019},{'name':'tesla','price':1000000,'amount':1}......]
# 练习1：
# count = 0
# l1 = []
# with open('a', mode='r', encoding='utf-8') as f:
#     for line in f:
#         dic = {}
#         line = line.strip()
#         line = line.split()
#         dic['name'] = line[0]
#         dic['price'] = line[1]
#         dic['amount'] = line[2]
#         count += int(line[1]) * int(line[2])
#         l1.append(dic)
#     print(l1)
#     print(count)
# a = 1
# l1 = []
# with open('a.txt',encoding='utf-8') as f1:
#     for line in f1:
#         dic = {}
#         # print(line,type(line))
#         line = line.strip()  # 'apple 10 3'
#         line_list = line.split()  # ['apple', '10', '3']
#         # print(line_list)
#         dic['name'] = line_list[0]
#         dic['price'] = line_list[1]
#         dic['amount'] = int(line_list[2])
#         l1.append(dic)
# print(l1)

# 方法二：
# l1 = []
# with open('a.txt',encoding='utf-8') as f1:
#     for line in f1:
#         line = line.strip()  # 'apple 10 3'
#         line_list = line.split()  # ['apple', '10', '3'，]
#         dic = {'name':line_list[0],'price':int(line_list[1]),'amount': int(line_list[2]),'year': line_list[3]}
#         l1.append(dic)
# print(l1)
# 上面两个代码：如果数据的列数增加了，就得给字典手动增加一个相应的键值对，麻烦。
# l1 = []
# name_list = ['name', 'price', 'amount', 'year','备注']
# with open('a.txt',encoding='utf-8') as f1:
#     for line in f1:
#         line_list = line.strip().split()
#         # print(line_list)  # ['apple', '10', '3']
#         dic = {}
#         for index in range(len(name_list)):
#             dic[name_list[index]] = line_list[index]
#         l1.append(dic)
# print(l1)


# 有如下文件：
# alex是老男孩python发起人，创建人。
#
# alex其实是人妖。
#
# 谁说alex是sb？
#
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
#
# 将文件中所有的alex都替换成大写的SB（文件的改的操作）。
# import os
# with open('alex自述', encoding='utf-8') as f1, \
#      open('alex自述.bak', mode='w', encoding='utf-8') as f2:
#     old_content = f1.read()
#     new_content = old_content.replace('alex', 'SB')
#     f2.write(new_content)
# os.remove('alex自述')
# os.rename('alex自述.bak', 'alex自述')
# 文件a1.txt内容(选做题)
# name:apple price:10 amount:3 year:2012
#
# name:tesla price:100000 amount:1 year:2013
#
# ​	通过代码，将其构建成这种数据类型：
# l1 = []
# with open('a1', mode='r', encoding='utf-8') as f:
#     for line in f:
#         dic = {}
#         line = line.strip()
#         line = line.split()
#         for i in range(4):
#             new_line = line[i].split(':')
#             dic[new_line[0]] = new_line[1]
#         l1.append(dic)
# print(l1)
        # print(line)
# ​	[{'name':'apple','price':10,'amount':3,year:2012},
#
# ​	{'name':'tesla','price':1000000,'amount':1}......]
#
# ​	并计算出总价钱。
#
# 文件a1.txt内容(选做题)
# 序号 部门 人数 平均年龄 备注
#
# 1 python 30 26 单身狗
#
# 2 Linux 26 30 没对象
#
# 3 运营部 20 24 女生多
#
# .......
#
# 通过代码，将其构建成这种数据类型：
# l1 = []
# with open('a1', mode='r', encoding='utf-8') as f:
#     for line in f:
#         dic = {}
#         line = line.strip()
#         line = line.split()
#         dic['序号'] = line[0]
#         dic['部门'] = line[1]
#         dic['人数'] = line[2]
#         dic['平均年龄'] = line[3]
#         dic['备注'] = line[4]
#         l1.append(dic)
#     print(l1)
# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},
#
# ......]