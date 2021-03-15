# def meet(sex):    #函数的定义：接受的参数：形式参数
#     print("拿出手机")
#     print("打开陌陌")
#     s1 = '性别{}'.format(sex)
#     print(s1)
#     print('左滑一下')
#     print('右滑一下')
#     print("找个漂亮的妹子")
#     print("问她,约不约啊!")
#     print("ok 走起")


# meet('女')    #函数的执行传的参数：实际参数
# 函数的传参
# 实参 形参
# A:实参角度：
# 1.位置参数：从左到右，一一对应
# 2.关键字参数 一一对应  meet(sex='女', age=25)
# 3.混合传参：一一对应，位置参数一定要在关键字参数的前面
# B:形参角度：
# 1.位置参数 与实参角度的位置参数是一种
# 2.默认值参数（设置意义：普遍经常使用的）  def meet(weight, sex, age='女'):
#
# 练习1：写一个函数，只接受两个int的参数，函数的功能是将较大的数放回
# def my_max(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
#
# res = my_max(55, 66)
# print(res)

# 三元运算符：简单的if else   c = a if a > b else b
# a = 10
# b = 20
# c = a if a > b else b
# print(c)

# def meet(weight, sex, age='女'):    #函数的定义：接受的参数：形式参数
#     print("拿出手机")
#     print("打开陌陌")
#     s1 = '性别{},年龄{},重量{}'.format(sex, age, weight)
#     print(s1)
#     print('左滑一下')
#     print('右滑一下')
#     print("找个漂亮的妹子")
#     print("问她,约不约啊!")
#     print("ok 走起")
#
#
# meet(110, sex='女', age=25)

# 练习2：传入两个字符串参数，将两个参数拼接完成后形成的结果返回
# def union_str(s1, s2):
#     return s1 + s2
#
#
# print(union_str(s1='jasjdja', s2='sjdba123'))

# 练习3：写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新的内容返回给调用者
# def check_len(li):
#     if len(li) <= 2:
#         return '列表长度小于2'
#     else:
#         return li[0:2]
#
#
# print(check_len([11]))
# print(check_len([11, 33, 55, 66]))
