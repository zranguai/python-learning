# 相关练习题
# 1，"1-2*(60+(-40.35/5)-(-4*3))"
import re
# res = "1-2*(60+(-40.35/5)-(-4*3))"
# 1.1 匹配所有的整数
# ret1 = re.findall('\d+', res)
# print(ret1)
# 1.2 匹配所有的数字（包含小数）
# ret2 = re.findall('\d+\.?\d*|\d*\.?\d+', res)
# print(ret2)
# 1.3 匹配所有的数字（包含小数包含负号）
# ret3 = re.findall('-?\d+\.?\d*|\-?\d*\.?\d+', res)
# print(ret3)
# 2,匹配一段你文本中的每行的邮箱
# http://blog.csdn.net/make164492212/article/details/51656638 匹配所有邮箱

# 3，匹配一段你文本中的每行的时间字符串 这样的形式：'1995-04-27'

s1 = '''
时间就是1995-04-27,2005-04-27
1999-04-27 老男孩教育创始人
老男孩老师 alex 1980-04-27:1980-04-27
2018-12-08
'''


# 4 匹配 一个浮点数


# 5 匹配qq号：腾讯从10000开始：
# print(re.findall('[1-9][0-9]{4,}', '2413545136'))

s1 = '''
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7459977.html" target="_blank">python基础一</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7562422.html" target="_blank">python基础二</a></p>
<p><a style="text-decoration: underline;" href="https://www.cnblogs.com/jin-xin/articles/9439483.html" target="_blank">Python最详细，最深入的代码块小数据池剖析</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7738630.html" target="_blank">python集合,深浅copy</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8183203.html" target="_blank">python文件操作</a></p>
<h4 style="background-color: #f08080;">python函数部分</h4>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8241942.html" target="_blank">python函数初识</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8259929.html" target="_blank">python函数进阶</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8305011.html" target="_blank">python装饰器</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8423526.html" target="_blank">python迭代器,生成器</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8423937.html" target="_blank">python内置函数,匿名函数</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8743408.html" target="_blank">python递归函数</a></p>
<p><a style="text-decoration: underline;" href="https://www.cnblogs.com/jin-xin/articles/8743595.html" target="_blank">python二分查找算法</a></p>
'''
# 1,找到所有的p标签
# ret = re.findall('<p>.*?</p>', s1)
# print(ret)

# 2,找到所有a标签对应的url
ret2 = re.findall('<p><a.*?href=(.*?)" target.*?</p>', s1)
print(ret2)

