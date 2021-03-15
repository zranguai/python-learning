# 练习1：池
# 1.线程池
# import time
# import random
# from concurrent.futures import ThreadPoolExecutor
#
# def func():
#     print('start')
#     time.sleep(random.randint(1, 2))
#     print('end')
#
# tp = ThreadPoolExecutor(8)
# for i in range(10):
#     tp.submit(func)

# 2.进程池
# import time
# import random
# from concurrent.futures import ProcessPoolExecutor
#
# def func():
#     print('start')
#     time.sleep(random.randint(1, 2))
#     print('end')
#
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(4)
#     for i in range(10):
#         tp.submit(func)


# 练习2：协程
# 1.gevent 协程例子
# import time
# import gevent
# from gevent import monkey
# monkey.patch_all()
#
# start = time.time()
# print(start)
# def func():
#     print('start func')
#     time.sleep(1)    # 遇到时间片就切出去
#     print('end func')
#
# g1 = gevent.spawn(func)
# g2 = gevent.spawn(func)
# g3 = gevent.spawn(func)
# gevent.joinall([g1, g2, g3])
# end = time.time()
# print(end)
# print(end - start)

# 2.asyncio
import asyncio
async def func(name):
    print('start')
    await asyncio.sleep(1)
    print('end')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([func('alex'), func('太白')]))







