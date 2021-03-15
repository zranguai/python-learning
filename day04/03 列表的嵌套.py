li = [1, 2, 'taibai', [1, 'alex', 3]]
# 1.将li中的'taibai‘变成大写并放回原处
# li[2] = li[2].upper()
# print(li)
# 2.给小列表[1, 'alex', 3]追加一个元素’老男孩教学‘
# li[3].append('老男孩教学')
# print(li)
# 3.将列表中的'alex'拼接成'alexsb'
li[3][1] = li[3][1] + 'sb'
print(li)