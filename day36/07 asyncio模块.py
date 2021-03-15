# 记住 *****
import asyncio
# async定义一个协程函数
async def func(name):
    print('start', name)
    # await 可能会发生阻塞的方法
    # await关键只必须写在一个async函数里
    await asyncio.sleep(1)    # 来回切
    print('end')

loop = asyncio.get_event_loop()
# loop.run_until_complete(func('alex'))
loop.run_until_complete(asyncio.wait([func('alex'), func('太白')]))
