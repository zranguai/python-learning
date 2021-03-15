# 集合的创建
# 方式1：
# set1 = set({1, 3, 'Barry', False})
# 方式2：直接创建
# set1 = {1, 3, 4, 'Barry', False, '哈哈'}
# print(set1)

# print({}, type({}))  #空字典
# set2 = set()
# print(type(set2))   #空集合

# 集合有效性测试 (里面元素应该为不可变类型)
# set3 = {[1, 2, 3], 5, 'kkk'}
# print(set3)

# set1 = {'哈哈', '呵呵', '嘿嘿', 'keke'}
# 增
# 1.add()
# set1.add('jj')
# print(set1)
# 2.update()迭代着增加
# set1.update('jjjssaase')
# print(set1)

# 删
# 1.remove()按照元素删除
# set1.remove('呵呵')
# print(set1)
# 2.pop() 随机删除
# set1.pop()
# print(set1)
# 变相改之
# set1.remove('哈哈')
# set1.add('jj')
# print(set1)


# 集合的其他操作
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# 1.交集
# print(set1.intersection(set2))
# 2.并集
# print(set1.union(set2))
# 3.差集
# print(set1.difference(set2))
# 4.反交集
# print(set1.symmetric_difference(set2))

# 5.子集
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5, 6}
# print(set1 < set2)
# 6.超集
# print(set2 > set1)

# 面试题：数组的去重
l1 = [1, 1, 2, 2, 2, 3, 4, 5, 6, 6, 6]
set1 = set(l1)
l1 = list(set1)
print(l1)
