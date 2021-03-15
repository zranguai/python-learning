dic = {
    'name': '汪峰',
    'age': 48,
    'wife': [{'name': '国际章', 'age': 38}],
    'children': {'girl_first': '小苹果', 'girl_second': '小怡', 'girl_three': '顶顶'}
}

# 1. 获取汪峰的名字。
print(dic['name'])
print(dic.get('name'))
# 2.获取这个字典：{'name':'国际章','age':38}。
print(dic['wife'][0])
# 3. 获取汪峰妻子的名字。
print(dic['wife'][0]['name'])
# 4. 获取汪峰的第三个孩子名字。
print(dic['children']['girl_three'])
