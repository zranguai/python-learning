# python并发编程之线程协程
## part 4:
### 异步阻塞例子与生产者消费者模型
+ 同步阻塞
	+ 调用函数必须等待结果\cpu没工作input  sleep  recv  accept connect  get
+ 同步非阻塞
	+ 调用函数必须等待结果\cpu工作-调用了一个高计算的函数stripeval('1+2+3')sum  max  min  sorted
+ 异步阻塞
	+ 调用函数不需要立即获取结果,而是继续做其他的事情,在获取结果的时候不知道先获取谁的,但是总之需要等(阻塞)
+ 异步非阻塞
  + 调用函数不需要立即获取结果,也不需要等start()  terminate()
```
import  requests
from  multiprocessing  import  Process, Queue

url_list={
	'zhipin':'https://www.zhipin.com/c101190400-p100101/',
	'cnblogs':'https://www.cnblogs.com/Eva-J/articles/8253549.html',
	'gitee':'https://gitee.com/zranguai/teaching_plan/blob/master/day34%20%E8%AF%BE%E5%A0%82%E7%AC%94%E8%AE%B0%E4%BB%A5%E5%8F%8A%E4%BB%A3%E7%A0%81/day34/1.%E5%86%85%E5%AE%B9%E5%9B%9E%E9%A1%BE.py',
	'baidu':'https://www.baidu.com/'
}
def  producer(name,url,q):
	ret=requests.get(url)
	q.put((name,ret.text))

def  consumer(q):
	while  True:
		tup=q.get()
		if  tup  is  None:break
		with  open(f'{tup[0]}.html',mode='w',encoding='utf-8')  as  f:
			f.write(tup[1])
if__name__=='__main__':
	q=Queue()
	p1=[]
	for  key  in  url_list:
		p=Process(target=producer,args=(key,url_list[key],q))
		p.start()
		p1.append(p)
	Process(target=consumer,args=(q,)).start()
	for  i  in  p1:
		i.join()
	q.put(None)
	#foriinrange(4):
#print(q.get())
```
### 通过Manager进行数据共享
```
from  multiprocessing  import  Process,Manager,Lock

def  change_dic(dic,lock):
	with  lock:
		dic['count']-=1

if__name__=='__main__':
	# 用法1：（常用）
	m=Manager()
	lock=Lock()
	dic=m.dict({'count':100})
	#dic={'count':100}
	p_l=[]
	for  i  in  range(100):
		p=Process(target=change_dic,args=(dic,lock))
		p.start()
		p_l.append(p)
	for  i  in  p_l:
		i.join()
	#print(dic)  #{'count':100}没有Manager不会改变，因为进程的数据之间相互独立
	print(dic)   #{'count':0}有Manager数据之间会共享
	
	#用法2：
	with  Manager()  as  m:
		lock = Lock()
		dic = m.dict({'count':100})
		#dic = {'count':100}
		p_l = []
		for  i  in  range(100):
			p=Process(target=change_dic,args=(dic,lock))
			p.start()
			p_l.append(p)
		for  i  in  p_l:
			i.join()
		#print(dic)  #{'count':100}没有Manager不会改变，因为进程的数据之间相互独立
print(dic)  #{'count':0}有Manager数据之间会共享
```
### 线程
+ 进程：数据隔离，资源分配的最小单位，可以利用多核，操作系统调度，数据不安全，开启关闭切换消耗大
	+ multiprocessing如何开启进程start  join
	+ 进程有数据不安全的问题Lock（抢票例子）
	+ 进程之间可以通信ipc
		+ 队列（安全）管道（不安全）
			+ 生产者消费者模型
		+ 第三方工具
	+ 进程之间可以通过Manager类实现数据共享（这里可以不需要写代码）
  + 一般情况下我们开启的进程数不会超过cpu个数的两倍
+ 线程（80%）
	+ 什么是线程：能被操作系统调度（给CPU执行）的最小单位
	+ 同一个进程中的多个线程同时被CPU执行？？？可能
	+ 数据共享，操作系统调度的最小单位，可以利用多核(在cpython中不能用多核)，操作系统调度，数据不安全，开启关闭切换消耗小
+ 在python中的多线程---节省io操作时间
	+ gc垃圾回收机制线程
		+ 引用计数+分代回收
	+ 全局解释器锁的出现主要是为了完成gc的回收机制，对不同线程的引用计数的变化记录的更加精准
	+ 全局解释器锁GIL（globalinterpreterlock）
		+ 导致了同一个进程中的多个线程只有一个线程真正被cpu执行

	+ 节省的是io操作的时间，而不是cpu计算的时间，因为cpu的计算速度非常快，我们没有办法把一条进程中所有的io操作都规避掉
### threading模块
+ 线程开启速度快,线程是并发，轮流在一个cpu上执行
####  方式1：
```
import  os
import  time
from  threading  import  Thread, current_thread, enumerate, active_count

def  func(i):
	print(f'start{i}',current_thread().ident)    #current_thread().ident拿线程的id
	time.sleep(1)
	print(f'end{i}')


if__name__=='__main__':
	t1=[]
	for  i  in  range(10):
		t = Thread(target=func,args=(i,))
		t.start()
		print(t.ident,os.getpid())#线程id不同进程id同
		t1.append(t)
	print(enumerate(),active_count())
	for  i  in  t1:
		i.join()
print('所有的线程都执行完了')
```
+ current_thread()获取当前所在的线程的对象  current_thread().ident通过ident可以获取线程id
+ 线程是不能从外部terminate
+ 所有的子线程只能是自己执行完代码之后才能关闭
+ enumerate列表存储了所有活着的线程对象,包括主线程
+ active_count数字存储了所有活着的线程个数
#### 方式2：
```
from  threading  import  Thread
class  MyThead(Thread):
	def  __init__(self,a,b):
		self.a=a
		self.b=b
		super().__init__()
	def  run(self):
		print(self.ident)

t = MyThead(1,2)
t.start()#开启线程，才在线程中执行run方法
print(t.ident)
```
### 线程之间数据是共享的
```
from  threading  import  Thread
n=100
def  func():
	global  n
	n -= 1

t_l=[]
for  i  in  range(100):
	t=Thread(target=func)
	t.start()
	t_l.append(t)
for  i  in  t_l:
	i.join()
print(n)    # 0 说明线程之间数据是共享的
```
## part 5:
### 守护线程
+ 守护进程会随着主进程的代码结束而结束
	+ 如果主进程代码结束之后还有其他子进程在运行,守护进程不守护
+ 守护线程随着主线程的结束而结束
	+ 如果主线程代码结束之后还有其他子线程在运行,守护线程也守护
+ 为什么?
	+ 守护进程和守护线程的结束原理不同
	+ 守护进程需要主进程来回收资源
	+ 守护线程是随着进程的结束才结束的
      + 其他子线程-->主线程结束-->主进程结束-->整个进程中所有的资源都被回收-->守护线程也会被回收
```
代码例子：
import  time
from  threading  import  Thread

def  son():
	while  True:
		print('inson')
		time.sleep(1)

def  son2():
	for  i  in  range(3):
		print('inson2****')
		time.sleep(1)
#问从flag a到flag b需要多长时间？答：0s多
#flag  a
t = Thread(target=son)
t.daemon = True
t.start()
Thread(target=son2).start()
#flagb
```
### 线程数据不安全现象
+ +=  -=  *=  /=  while  if数据不安全+和赋值是分开的两个操作
+ append  pop  strip数据安全列表中的方法或者字典中的方法去操作全局变量的时候数据安全的
+ 线程之间也存在数据不安全
#### 数据不安全例子
```
from  threading  import  Thread

n=0
def  add():
	for  i  in  range(500000):
		global n
		n += 1
def  sub():
	for  i  in  range(500000):
		global n
		n  -=  1

t_l = []
for i in range(2):
	t1=Thread(target=add)
	t1.start()
	t2 = Thread(target=sub)
	t2.start()
	t_l.append(t1)
	t_l.append(t2)
for t in t_l:
	t.join()
print(n)
-----------------
原因：+= -= GIL锁切换了
import  dis
a=0
def  func():
	global  a
	a + =1
	dis.dis(func)

'''
56   0 LOAD_GLOBAL  0(a)
	2 LOAD_CONST1(1)
	4 INPLACE_ADD
	#GIL锁切换了
	6 STORE_GLOBAL0(a)
'''
```
#### 线程安全例子
```
from  threading  import  Thread
import  time
n=[]
def  append():
	for i in range(500000):
		n.append(1)
def  pop():
	for i in range(500000):
		if  not  n:
			time.sleep(0.0000001)
		n.pop()

t_l = []
for i in range(20):
	t1 = Thread(target=append)
	t1.start()
	t2 = Thread(target=pop)
	t2.start()
	t_l.append(t1)
	t_l.append(t2)
for t in t_l:
	t.join()
print(n)
-------------------------
import  dis
a=[]
def  func():
	a.append(1)

dis.dis(func)

'''
70   0  LOAD_GLOBAL     0(a)
	2 LOAD_ATTR          1(append)
	4 LOAD_CONST        1(1)
	6 CALL_FUNCTION   1
	8 POP_TOP
'''
```
### 线程锁
+ 不要操作全局变量,不要在类里操作静态变量就不用加锁了
+ +=  -=  *=  /=  if  while数据不安全
+ queue  logging  数据安全的（内部已经实现了数据安全）
#### 线程加锁
```
from threading import Thread, Lock
n = 0
def add(lock):
    for i in range(500000):
        global n
        with lock:
            n += 1
def sub(lock):
    for i in range(500000):
        global n
        with lock:
            n -= 1

t_l = []
lock = Lock()
for i in range(2):
    t1 = Thread(target=add,args=(lock,))
    t1.start()
    t2 = Thread(target=sub,args=(lock,))
    t2.start()
    t_l.append(t1)
    t_l.append(t2)
for t in t_l:
    t.join()
print(n)
```
### 单例模式
```
# 线程安全的单例模式要默写
import time
class A:
    from threading import Lock
    __instance = None
    lock = Lock()
    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                time.sleep(0.000001)    # cpu轮转
                cls.__instance = super().__new__(cls)
        return cls.__instance

def func():
    a = A()
    print(a)
from threading import Thread
for i in range(10):
    Thread(target=func).start()
```
### 互斥锁和递归锁
```
from threading import Lock, RLock
Lock 互斥锁    效率高
RLock 递归(recursion)锁  效率相对低

l = Lock()
l.acquire()
print('希望被锁住的代码')
l.release()

rl = RLock()  # 在同一个线程中可以被acquire多次
rl.acquire()
rl.acquire()
print('希望被锁住的代码')
rl.release()    # 有多少次的acquire就要有多少次的release,要不然别人进不去
```
+ 即：
```
from threading import Thread, RLock as Lock

def func(i,lock):
    lock.acquire()
    lock.acquire()
    print(i,': start')
    lock.release()
    lock.release()
    print(i, ': end')

lock = Lock()
for i in range(5):
    Thread(target=func, args=(i, lock)).start()
```
### 死锁现象
```
死锁现象是怎么产生的? **
    多把(互斥/递归)锁 并且在多个线程中 交叉使用
            fork_lock.acquire()
            noodle_lock.acquire()

            fork_lock.release()
            noodle_lock.release()
    如果是互斥锁,出现了死锁现象,最快速的解决方案把所有的互斥锁都改成一把递归锁
         程序的效率会降低的
    递归锁 效率低 但是解决死锁现象有奇效**
    互斥锁 效率高 但是多把锁容易出现死锁现象**

    一把互斥锁就够了（解决80%问题）
```
### 队列
#### 先进先出队列
```
import queue    # 线程之间数据安全的容器队列
from queue import Empty    # 不是内置的错误类型，而是queue模块中的错误

q = queue.Queue(4)    # fifo 先进先出队列
# q.get()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
print('4 done')

# q.put(5)
# print('5 done')
try:
    q.get_nowait()
except Empty:
    pass
print('队列为空，继续其他内容')
```
####  last in first out
```
from queue import LifoQueue    # last in first out 后进先出  栈
lq = LifoQueue()
lq.put(1)
lq.put(2)
lq.put(3)
print(lq.get())
print(lq.get())
print(lq.get())
```
#### 优先级队列
```


from queue import PriorityQueue    # 优先级队列

priq = PriorityQueue()
priq.put((2, 'alex'))
priq.put((1, 'wusir'))
priq.put((3, '太白'))

print(priq.get())
print(priq.get())
print(priq.get())
```
## part 6:
### 池
+ 有多少个任务就开多少个进程或者线程
+ **什么是池？**
    + 要在程序开始的时候，还没提交任务先创建几个进程或者线程
    + 放在一个池子里，这就是池，放线程就是线程池，放进程就是进程池

+ 为什么要用池?
    + 如果先开好进程/线程,那么有任务之后就可以直接使用这个池中的数据了
    + 并且开好的线程或者进程会一直存在在池中,可以被多个任务反复利用
        + 这样极大的减少了开启\关闭\调度线程/进程的时间开销
    + 池中的线程/进程个数控制了操作系统需要调度的任务个数,控制池中的单位
        + 有利于提高操作系统的效率,减轻操作系统的负担
+ 发展过程
  + threading模块 没有提供池
  + multiprocessing模块 仿照threading写的 Pool
  + concurrent.futures模块 线程池,进程池都能够用相似的方式开启\使用
#### 线程池：
```
# 线程池：
import time
import random
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor

def func(a, b):
    print(current_thread().ident, 'start', a, b)
    time.sleep(random.randint(1, 4))
    print(current_thread().ident, 'end')

# 先开4个线程，其中有线程结束时会有新的线程进去，始终使用开启的4个线程
if __name__ == '__main__':
    tp = ThreadPoolExecutor(4)    # 在该线程池中开4个线程
    for i in range(10):
        tp.submit(func, i, i+1)    # (传递参数) 把任务提交给池，池替你执行线程中的任务
```
#### 进程池：
```
# 进程池：
import time
import random
import os
from concurrent.futures import ProcessPoolExecutor

def func(a, b):
    print(os.getpid(), 'start', a, b)
    time.sleep(random.randint(1, 4))
    print(os.getpid(), 'end')

# 先开4个进程，其中有进程结束时会有新的进程进去，始终使用开启的4个进程
if __name__ == '__main__':
    tp = ProcessPoolExecutor(4)    # 在该进程池中开4个进程程
    for i in range(10):
        tp.submit(func, i, i+1)    # (传递参数) 把任务提交给池，池替你执行进程中的任务
```
#### 获取任务结果：
```
# 获取任务结果：
import time
import random
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def func(a, b):
    print(os.getpid(), 'start', a, b)
    time.sleep(random.randint(1, 4))
    print(os.getpid(), 'end')
    return a * b

if __name__ == '__main__':
    tp = ProcessPoolExecutor(4)
    future_l = {}
    for i in range(10):    # 异步非阻塞
        ret = tp.submit(func, i, i+1)
        # print(ret.result())    # Future对象（现在放进去，未来才用到）
        future_l[i] = ret
    for key in future_l:    # 这里获取结果时同步的
        print(key, future_l[key].result())
```
####  map
```
# map  tp对象的map 只适合传递简单的参数，并且必须是一个可迭代的类型作为参数
import time
import random
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def func(a):
    b = a + 1
    print(os.getpid(), 'start', a, b)
    time.sleep(random.randint(1, 4))
    print(os.getpid(), 'end')
    return a * b


if __name__ == '__main__':
    tp = ProcessPoolExecutor(4)
    ret = tp.map(func, range(20))
    for key in ret:
        print(key)
```
#### 回调函数： 效率最高
```
# 回调函数： 效率最高
import time
import random
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor

def func(a, b):
    # print(current_thread().ident, 'start', a, b)
    time.sleep(random.randint(1, 4))
    # print(current_thread().ident, 'end')
    return (a, a * b)
def print_func(ret):    # 回调过程 异步阻塞
    print(ret.result())

if __name__ == '__main__':
    tp = ThreadPoolExecutor(4)
    future_l = {}
    for i in range(20):    # 异步非阻塞的
        ret = tp.submit(func, i, i+1)
        # ret这个任务会在执行完毕的瞬间立即触发print_func函数，并且把任务的返回值对象传递到print_func做参数
        ret.add_done_callback(print_func)    # 异步阻塞
        # 异步阻塞 回调函数 给ret对象绑定一个回调函数，等待ret对应的任务有了结果之后立即调用print_func这个函数
        # 就可以对结果立即进行处理，而不用按照顺序接受结果处理结果
```
### 回调函数的例子
```
from concurrent.futures import ThreadPoolExecutor
import requests
import os

def get_page(url):    # 访问网页,获取网页源代码   线程池中的线程来操作
    print('<进程%s> get %s' %(os.getpid(), url))
    respone=requests.get(url)
    if respone.status_code == 200:
        return {'url': url, 'text': respone.text}

def parse_page(res):   # 获取到字典结果之后,计算网页源码的长度,把https://www.baidu.com : 1929749729写到文件里   线程任务执行完毕之后绑定回调函数
    res = res.result()
    print('<进程%s> parse %s' %(os.getpid(),res['url']))
    parse_res = 'url:<%s> size:[%s]\n' %(res['url'],len(res['text']))
    with open('db.txt', 'a') as f:
        f.write(parse_res)

if __name__ == '__main__':
    urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]
    # 获得一个线程池对象 = 开启线程池
    tp = ThreadPoolExecutor(4)    # 起池
    # 循环urls列表
    for url in urls:
        # 得到一个futrue对象 = 把每一个url提交一个get_page任务
        ret = tp.submit(get_page, url)    # 1.提交的任务 2.传递的参数    # 提交任务
        # 给futrue对象绑定一个parse_page回调函数
        ret.add_done_callback(parse_page)   # 谁先回来谁就先写结果进文件
# 不用回调函数:
    # 按照顺序获取网页 百度 python openstack git sina
    # 也只能按照顺序写
# 用上了回调函数
    # 按照顺序获取网页 百度 python openstack git sina
    # 哪一个网页先返回结果,就先执行那个网页对应的parserpage(回调函数)
```
# 协程
## 协程概念：
```
# 进程
# 线程
    # 正常的开发语言 多线程可以利用多核
    # cpython解释器下的多个线程不能利用多核：规避了所有io操作的单线程
# 协程：
    # 是操作系统不可见的
    # 协程本质就是一条线程 多个任务在一条线程上来回切换，
    # 利用协程这个概念实现的内容：来规避io操作，就达到了我们将一条线程中的io操作降到最低的目的

# 切换 并 规避io的两个模块
# gevent = 利用了 greenlet    底层模块完成的切换 + 自动规避io的功能
# ayncio = 利用了 yield       底层语法完成的切换 + 自动规避io的功能
    # tornado 异步的web框架
    # yield from - 更好的实现协程
    # send - 更好的实现协程
    # asyncio模块 基于python原生的协程的概念正式的被成立
    # 特殊的在python中提供协程功能的关键字： aysnc await

# *****
# 进程 数据隔离 数据不安全  操作系统级别  开销非常大  能利用多核
# 线程 数据共享 数据不安全  操作系统级别  开销小      (cpython解释器)不能利用多核   一些和文件操作相关的io只有操作系统能感知到
# 协程 数据共享 数据安全    用户级别      更小        不能利用多核   协程的所有的切换都基于用户，只有在用户级别能够感知到的io才会用协程模块做切换来规避（socket，请求网页的）

# 用户级别的协程还有什么好处：
    # 减轻了操作系统的负担
    # 一条线程如果开了多个协程，那么给操作系统的印象是线程很忙，这样能多争取一些时间片时间来被CPU执行,程序的效率就提高了
```
## gevent-协程例子
```
# 理解
from gevent import monkey
monkey.patch_all()
import time
import gevent

def func():    # 带有io操作的内容写在函数里，然后提交func给gevent
    print('start func')
    time.sleep(1)    # 有io操作就切换出去
    print('end func')


g1 = gevent.spawn(func)    # spawn 再生，产生
g2 = gevent.spawn(func)    
g3 = gevent.spawn(func)    
gevent.joinall([g1, g2, g3])
```
## asyncio模块
```
# 记住 *****
import asyncio
# async定义一个协程函数
async def func(name):
    print('start', name)
    # await 可能会发生阻塞的方法
    # await关键只必须写在一个async函数里
    await asyncio.sleep(1)    # 来回切
    print('end')

loop = asyncio.get_event_loop()
# loop.run_until_complete(func('alex'))
loop.run_until_complete(asyncio.wait([func('alex'), func('太白')]))
```
