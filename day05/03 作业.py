# 1.请将列表中的每个元素通过 "_" 链接起来。
#
# users = ['李少奇', '李启航', '渣渣辉']
# 请将列表中的每个元素通过 "_" 链接起来。
# str1 = '_'.join(users)
# print(str1)
#
# 2.请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。
#
# v1 = (11, 22, 33)
# v2 = [44, 55, 66]
# v2.extend(v1)
# print(v2)
#
# # 请将元组 v1 = (11,22,33,44,55,66,77,88,99) 中的所有偶数索引位置的元素 追加到列表 v2 = [44,55,66] 中
# v1 = (11, 22, 33, 44, 55, 66, 77, 88, 99)
# v2 = [44, 55, 66]
# v2.extend(v1[::2])
# print(v1)
# print(v2)
# 3.将字典info = {'k1':'v1','k2':'v2','k3':'v3'}的键和值分别追加到 key_list 和 value_list 两个列表中，如：
#
# info = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# key_list = []
# value_list = []
# key_list.extend(info.keys())
# value_list.extend(info.values())
# print(key_list)
# print(value_list)
#
# 4.字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
# a. 请循环输出所有的key
# for i in dic.keys():
#     print(i)
# b. 请循环输出所有的value
# for i in dic.values():
#     print(i)
# c. 请循环输出所有的key和value
# for i in dic.items():
#     print(i[0])
#     print(i[1])
# d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic.setdefault('k4', 'v4')
# print(dic)
# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)
# f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
# dic['k3'].append(44)
# print(dic)
# g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
# dic.get('k3').insert(1, 18)
# print(dic)
#
# 5.
av_catalog = {
    "欧美": {
        "www.太白.com": ["很多免费的,世界最大的", "质量一般"],
        "www.alex.com": ["很多免费的,也很大", "质量挺好"],
        "oldboy.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "hao222.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}
# 给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'量很大'。
# av_catalog["欧美"]["www.太白.com"].append('量很大')
# 将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# av_catalog["欧美"]["hao222.com"].remove("全部收费,屌丝请绕过")
# 将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# av_catalog["日韩"]["tokyo-hot"][1] = av_catalog["日韩"]["tokyo-hot"][1].upper()
# 给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# av_catalog["大陆"].setdefault('1048', ['一天就封了'])
# 删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
# av_catalog["欧美"].pop("oldboy.com")
# 给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# av_catalog["大陆"]["1024"][0] = av_catalog["大陆"]["1024"][0] + '可以爬下来'
# print(av_catalog)
#
# 6.请循环打印k2对应的值中的每个元素。
#
# info = {
#     'k1': 'v1',
#     'k2': [('alex'), ('wupeiqi'), ('oldboy')],
# }
# for i in info['k2']:
#     print(i)
#
# 7.有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}
#
# dic = {}
# s = "k: 1|k1:2|k2:3 |k3 :4"
# s1 = s.split('|')
# for i in s1:
#     s2 = i.split(':')
#     dic[s2[0]] = int(s2[1])
# print(dic)
# 8.写代码
# """
# 有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
# result = {'k1':[],'k2':[]}
#
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# result = {'k1': [], 'k2': []}
# for i in li:
#     if i > 66:
#         result['k1'].append(i)
#     else:
#         result['k2'].append(i)
# print(result)
# 9."""
# 输出商品列表，用户输入序号，显示用户选中的商品
#
# """
# 商品列表：
# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998}
# ]
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如：
#       1 电脑 1999
#       2 鼠标 10
# 	  ...
# for i in range(0, len(goods)):
#     print(str(i + 1) + ' ' + goods[i]['name'] + ' ' + str(goods[i]['price']))
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# ind = int(input('请输入商品序号'))
# res = '商品名称是{0},商品价格是{1}'.format(goods[ind]['name'], goods[ind]['price'])
# print(res)
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# index = int(input('请输入商品序号'))
# while True:
#     if 0 <= index <= len(goods):
#         print(index)
#         break
#     else:
#         print('请重新输入')
#         index = int(input('请输入商品序号'))
# 4：用户输入Q或者q，退出程序。
# """
# while True:
#     inp = input('请输入')
#     if inp.upper() == 'Q':
#         break
# 10看代码写结果
#
# v = {}
# for index in range(10):
#     v['users'] = index
# print(v)
# {'users': 9}

# 补充：枚举类型enumerate（）
# li = ['alex','银角','女神','egon','太白']
# for i in enumerate(li):
#     print(i)
# for index,name in enumerate(li,1):
#     print(index,name)
# for index, name in enumerate(li, 100):  # 起始位置默认是0，可更改
#     print(index, name)