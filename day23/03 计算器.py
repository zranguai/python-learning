# day23 第二个视频，写完计算器作业再来看
# 这周周五交计算器作业
# exp = ' 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式的计算器程序'
exp = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# 先匹配小括号里的内容
# 然后先计算乘除法
# 再计算加减法
import re
# 计算加减法
exp = '1+2.238-317+428-5+6'
def remove_addsub(exp):
    ret = re.findall('[-+]?\d+(?:\.\d+)?', exp)
    print(ret)
    count = 0
    for i in ret:
        count += float(i)
    print(count)
    return count
remove_addsub(exp)

# 计算两个数的的乘法或者除法
def mul_div(exp):
    if '*' in exp:
        a,b = exp.split('*')
        return float(a) * float(b)
    if '/' in exp:
        a, b = exp.split('/')
        return float(a) / float(b)

# 计算乘除法
def remove_muldiv(exp):
    while True:
        ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', exp)
        if ret:
            son_exp = ret.group()  # 3*4 12*5
            res = mul_div(son_exp)
            print(res) # 12 60
            exp = exp.replace(son_exp, str(res))
            print('-->', exp)    # exp = 1+12.0*5/6
        else:
            break
        return exp

ret = remove_muldiv('1+3*4*5/6-4-7')
print(ret)
# 用循环用正则
# 调用函数


# def cal_mul():    # 乘
#     # exp = 4*6
#     # logging.debug('4*6 = 24')
#     # return 24
#     pass
# def cal_div():    # 除
#     pass
# def cal_add():    # 加
#     pass
# def cal_sub():    # 减法
#     pass
# def cal_inner_bracket(exp2):    # 调用里面
#     # exp = 3 - 4 * 6
#     # cal_mul(4 * 6)
#     pass
# def main(exp):
#     # exp = (1 + 2 * (3 - 4 * 6)) / 5
#     # cal_inner_bracket(3 - 4 * 6)
#     pass


# 计算一个带着加减乘除四则运算的表达式
# 做去括号

