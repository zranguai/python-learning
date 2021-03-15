# 分组命名
# (?P<名字>正则表达式)
# ret.group('名字')
# import re
# ret = re.search('\d(\d)\d(\w+?)(\d)(\w)\d(\d)\d(?P<name1>\w+?)(\d)(\w)\d(\d)\d(?P<name2>\w+?)(\d)(\w)',
#           '123abc45678agsf_123abc45678agsf123abc45678agsf')
#
# print(ret.group('name1'))
# print(ret.group('name2'))


# 分组命名的引用（一般使用这个）
# import re
# exp = '<abc>akda65485*11</abc>asdjasd5a</abd>'
# ret = re.search('<(?P<tag>\w+)>.*?</(?P=tag)>', exp)
# print(ret)


# 不希望他在python中转义用r'',  加r取消转义
# 分组的索引引用（使用的不多）  python中\1有特殊意义，可以通过在前面加r取消特殊意义
# import re
# exp = '<abc>akda65485*11</abc>asdjasd5a</abd>'
# ret = re.search(r'<(\w+)>.*?</\1>', exp)   # \1取消在python中的特殊意义，加r体现在正则中的意义
# print(ret)

print('\p')
print(r'\b')
print('\s')



















