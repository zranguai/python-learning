# 1.匹配一篇英文文章的标题 类似 The Voice Of Chona
# 2.匹配一个网址
# 3.匹配年月日日期 类似 2018-12-06 2018/12/06 2018.12.06
# 4.匹配15位或者18位身份证号码
# 链家例子：

par = '<div class="title">.*?<a class=.*?>(?P<name>.*?)</a>.*?<span class="divide">/</span>(?P<room>.*?)<span class="divide">/</span>(?P<area>.*?)<span'
import re
with open('lianjia.html', encoding='utf-8') as f:
    content = f.read()
res = re.findall(par, content, flags=re.S)
print(res)
# ret = re.finditer(par, content, flags=re.S)
# for i in ret:
#     print(i.group('name'))
#     print(i.group('room'))
#     print(i.group('area'))




