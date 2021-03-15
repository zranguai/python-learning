# 异步阻塞例子与生产者消费者模型
import requests
from multiprocessing import Process, Queue


url_list = {
    'zhipin': 'https://www.zhipin.com/c101190400-p100101/',
    'cnblogs': 'https://www.cnblogs.com/Eva-J/articles/8253549.html',
    'gitee': 'https://gitee.com/zranguai/teaching_plan/blob/master/day34%20%E8%AF%BE%E5%A0%82%E7%AC%94%E8%AE%B0%E4%BB%A5%E5%8F%8A%E4%BB%A3%E7%A0%81/day34/1.%E5%86%85%E5%AE%B9%E5%9B%9E%E9%A1%BE.py',
    'baidu': 'https://www.baidu.com/'
}
def producer(name, url, q):
    ret = requests.get(url)
    q.put((name, ret.text))


def consumer(q):
    while True:
        tup = q.get()
        if tup is None: break
        with open(f'{tup[0]}.html', mode='w', encoding='utf-8') as f:
            f.write(tup[1])
if __name__ == '__main__':
    q = Queue()
    p1 = []
    for key in url_list:
        p = Process(target=producer, args=(key, url_list[key], q))
        p.start()
        p1.append(p)
    Process(target=consumer, args=(q, )).start()
    for i in p1:
        i.join()
    q.put(None)
    # for i in range(4):
    #     print(q.get())




# 同步阻塞
#     调用函数必须等待结果\cpu没工作 input sleep recv accept connect get
# 同步非阻塞
#     调用函数必须等待结果\cpu工作 - 调用了一个高计算的函数 strip eval('1+2+3') sum max min sorted
# 异步阻塞
#     调用函数不需要立即获取结果,而是继续做其他的事情,在获取结果的时候不知道先获取谁的,但是总之需要等(阻塞)
# 异步非阻塞
#      调用函数不需要立即获取结果,也不需要等 start() terminate()


