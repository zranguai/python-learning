# 6天
# 操作系统基础 1天
# 进程 2天
# 线程 2天
# 协程 1天

# 30min
# 3h
# 5min
# 3h35min 3h
# 人机矛盾 : cpu 100%工作

# 纸带读的慢,高速磁带
# 电子管
# 3min
# 30min
# 1min
# 36min 4min

# I/O操作 ： 相对内存来说
# 输入Input输出Output
# 输入是怎么输入 :键盘\input\read\recv
# 输出是怎么输出 :显示器 打印机 播放音乐\print\write\send
# 文件操作 :read write
# 网络操作 :send recv recvfrom
# 函数     :print input

# 计算机的工作分为两个状态
#     CPU工作   : 做计算(对内存中的数据进行操作)的时候工作
#     CPU不工作 : IO操作的时候
# CPU的工作效率 500000条指令/ms

# 多道操作系统 :一个程序遇到IO就把CPU让给别人
#     顺序的一个一个执行的思路变成
#     共同存在在一台计算机中,其中一个程序执行让出cpu之后,另一个程序能继续使用cpu
#     来提高cpu的利用率
#
#     单纯的切换会不会占用时间 : 会
#     但是多道操作系统的原理整体上还是节省了时间,提高了CPU的利用率
#     时空复用的概念


# 单cpu 分时操作系统 : 把时间分成很小很小的段,每一个时间都是一个时间片,
# 每一个程序轮流执行一个时间片的时间,自己的时间片到了就轮到下一个程序执行 -- 时间片的轮转
# 没有提高CPU的利用率 \ 提高了用户体验
#     老教授 24h全是计算 没有io
#         先来先服务 FCFS
#     研究生 5min全是计算 没有io
#         短作业优先
#     研究生2 5min全是计算 没有io

# 老教授 1min
# 研究生 1min
# 老教授 1min
# 研究生 1min
# 研究生2 1min   # 来了
# 老教授 1min
# 研究生 1min
# 研究生2 1min
# 老教授 1min
# 研究生 1min     # 执行完毕 10min
# 研究生2 1min
# 老教授 1min
# 研究生2 1min    # 执行完毕  9min
# 老教授 1min


# 实时操作系统


# 分布式
    # 操作系统
    # 程序 \ 插件软件
        # celery python分布式框架




