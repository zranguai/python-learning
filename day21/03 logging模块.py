# 为什么要写log?
# 1.log是为了排错
# 2.log用来做数据分析

# 购物商城 --数据库里
# 1.什么时间买了什么商品
# 2.把那些商品加入了购物车


# 做数据分析的内容 ---记录到日志
# 1.一个用户什么时间在什么地点 登入了购物程序
# 2.搜索了那些信息
# 3.什么时候关闭了软件
#  4.对那些商品点进去看了


# 对程序进行排错


# 使用日志：
# 1.用来记录用户的行为---数据分析
# 2.用来记录用户的行为---操作审计
# 3.排查代码中的错误




# import logging
# 输出内容是有等级的：默认处理warning级别以上的所有信息
# logging.debug('debug message')        # 调试
# logging.info('info message')          # 信息
# logging.warning('warning message')    # 警告
# logging.error('error message')        # 错误
# logging.critical('critical message')  # 批判性的


def cal_mul():
    # exp = 4*6
    # logging.debug('4*6 = 24')
    # return 24
    pass
def cal_div():
    pass
def cal_add():
    pass
def cal_sub():
    pass
def cal_inner_bracket(exp2):
    # exp = 3 - 4 * 6
    # cal_mul(4 * 6)
    pass
def main(exp):
    # exp = (1 + 2 * (3 - 4 * 6)) / 5
    # cal_inner_bracket(3 - 4 * 6)
    pass

# logging.basicConfig(level=logging.DEBUG)  # 调用这个会打印日志
# main('(1+2*(3-4*6))/5')





# 1.无论你希望日志里打印那些内容，都得你自己写，没有自动生成日志这件事

# logging.basicConfig  # asctime:时间 name：什么用户 levelname：日志等级 lineno:哪一行  module：什么文件 message：自己打印什么信息
# 输出到控制台
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)s] -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     # level=logging.ERROR
# )
#
# logging.warning('warning message test2')
# logging.error('error message test2')
# logging.critical('critical message test2')


# 输出到文件,并且设置信息的等级
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)s] -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     filename='tmp.log',
#     level=logging.DEBUG
# )
#
# logging.warning('warning message test2')
# logging.error('error message test2')
# logging.critical('critical message test2')


# -------------------------------------------------------------->>记下面
# 开始写
# 1.乱码
# 2.为什么不能同时向屏幕和屏幕输出
# fh = logging.FileHandler('tmp.log', encoding='utf-8')  # 输出到文件
# sh = logging.StreamHandler()    # 输出到屏幕
# logging.basicConfig  # asctime:时间 name：什么用户 levelname：日志等级 lineno:哪一行  module：什么文件 message：自己打印什么信息
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)s] -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level=logging.DEBUG,
#     handlers=[fh, sh]
# )
#
# logging.debug('debug ')
# logging.warning('warning message test2')
# logging.error('error message test2')
# logging.critical('critical message test2')

# 程序工作一段时间后写
# 日志的切分
# import time
# from logging import handlers
# # 每maxBytes切一个文件  backupCount=5：最多保留5个文件。在第6个时删除第一个文件
# rh = handlers.RotatingFileHandler('myapp.log', maxBytes=1024, backupCount=5)   # 按照大小进行切割
# # when='s'：按照秒来切 interval=5：每5秒切一个
# fh = handlers.TimedRotatingFileHandler(filename='x2.log', when='s', interval=5, encoding='utf-8')
#
# fh = logging.FileHandler('tmp.log', encoding='utf-8')
# sh = logging.StreamHandler()
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s[line:%(lineno)s] -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level=logging.DEBUG,
#     handlers=[fh, sh]
# )
#
# for i in range(1, 10):
#     time.sleep(1)
#     logging.error(f'error{str(i)}')

