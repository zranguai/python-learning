# 制作一个公共的模板
# 让一个字符串的某些位置可以动态传入
# 格式化输出
# name = input('请输入你的名字')
# age = input('请输入你的年龄')
# job = input('请输入你的工作')
# hobby = input('请输入你的爱好')
# # %占位符 s->str
# msg = '''------------ifo of %s -----------
# name : %s
# age : %s
# job : %s
# hobby : %s
# ''' % (name, name, age, job, hobby)
# print(msg)
# 在格式化输出中，%只想表示百分号而不是占位符，需要用%%来表示
msg = '我叫%s,今年%d,学习进度1%%' % ('李明', 16)
print(msg)