# 统计字符串的个数
# s1 = 'sadh0'


# count = 0
# for i in s1:
#     count += 1
# print(count)
# s1 = 'ajsdgacdasbcasgdjn'
# l1 = [1, 2, 3, 5, 6, 9, 8, 4]
#
#
# def my_len(s):
#     count = 0
#     for i in s:
#         count += 1
#     print(count)
#
#
# my_len(s1)
# my_len(l1)
#
# 函数的作用：
# 函数以功能（完成一件事）为导向
# 随调随用 减少代码重复性
# 增强代码可读性

# 函数的返回值
# return: 在函数中遇到return直接结束函数
# return 将数据返回给函数的执行者（调用）
# return 如果返回多个元素 是以元组的形式返回给函数的执行者
def meet():
    print("拿出手机")
    print("打开陌陌")
    print('左滑一下')
    print('右滑一下')
    print("找个漂亮的妹子")
    print("问她,约不约啊!")
    print("ok 走起")
    # return '哈哈哈'
    return '妹子', 123, [1, 2, 3]

# ret = meet()
# print(ret)
ret = meet()
# ret1, ret2, ret3 = meet()  #元组的拆包
print(ret, type(ret))

