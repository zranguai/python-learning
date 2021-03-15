# 可以通过Manager进行数据共享
from multiprocessing import Process, Manager, Lock

def change_dic(dic, lock):
    with lock:
        dic['count'] -= 1


if __name__ == '__main__':
    # 用法1：
    # m = Manager()
    # lock = Lock()
    # dic = m.dict({'count': 100})
    # # dic = {'count': 100}
    # p_l = []
    # for i in range(100):
    #     p = Process(target=change_dic, args=(dic, lock))
    #     p.start()
    #     p_l.append(p)
    # for i in p_l:
    #     i.join()
    # # print(dic)    # {'count': 100} 没有Manager不会改变，因为进程的数据之间相互独立
    # print(dic)    # {'count': 0} 有Manager 数据之间会共享

    # 用法2：
    with Manager() as m:
        lock = Lock()
        dic = m.dict({'count': 100})
        # dic = {'count': 100}
        p_l = []
        for i in range(100):
            p = Process(target=change_dic, args=(dic, lock))
            p.start()
            p_l.append(p)
        for i in p_l:
            i.join()
        # print(dic)    # {'count': 100} 没有Manager不会改变，因为进程的数据之间相互独立
        print(dic)  # {'count': 0} 有Manager 数据之间会共享




