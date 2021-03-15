# 列表的创建
# 方式一
# li = [1, 2, 'alex']

# 方式2
# li = list()
# li = list('123456')
# print(li, type(li))

# 方式3：列表推导式

# 增删改查
# li = ['哈哈', '嘿嘿', '呵呵']
# 增

# 1.append
# li.append('xx')
# print(li)
# 举例：
# li = ['哈哈', '嘿嘿', '呵呵']
# while True:
#     name = input('请输入:输入q/Q退出')
#     if name.upper() == 'Q':
#         break
#     li.append(name)
# print(li)

# 2.insert
# li = ['哈哈', '嘿嘿', '呵呵']
# li.insert(1, '哈哈哈')
# print(li)

# 3.extend:迭代者增加(一个元素)  一个一个的加上去
# li.extend('abcs5')
# li.extend(['ak48'])
# print(li)

# 删除
# 1.pop按照索引位置删除
# li = ['哈哈', '嘿嘿', '呵呵']
# li.pop(-1)  # 有返回值，返回的是删除的元素
# print(li.pop(-1))
# li.pop() # 默认删除最后一个
# print(li)

# 2.remove 按照指定元素去删除,如果由重名元素，默认删除第一个
# li.remove('哈哈')
# print(li)

# 3.clear() 清空所有[了解]
# li.clear()
# print(li)

# 4.del    1)按照索引删除 2.按照切片删除
# del li[-1]
# print(li)
# del li[::2]
# print(li)

# 改
# li = ['哈哈', '嘿嘿', '呵呵']
# 按照索引改
# li[0] = '哈韩'
# print(li)
# 按照切片改（了解）
# li[1:] = 'kkkk'
# print(li)
# 按照切片步长改值（必须一一对应）

# 查
# 索引  切片
# for i in li:
#     print(i)


# 练习题：
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 计算列表的长度并输出
# print(len(li))
# 列表中追加元素"seven",并输出添加后的列表
# li.append('seven')
# print(li)
# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# li.insert(1, 'Tony')
# print(li)
# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li[1] = 'Kelly'
print(li)