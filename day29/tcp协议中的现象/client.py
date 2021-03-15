# 粘包现象：本来分开的数据粘合到一起去了
# 只出现在tcp协议中,因为tcp协议 多条消息之间没有边界，并且还有一大推优化算法
# 发送端：两条消息都很短，发送的间隔时间也非常短
# 接收端：多条消息由于没有及时接受，而在接受方的缓存短，堆在一起导致的粘包
# tcp协议数据之间没有边界，可以传输大的数据

# 解决粘包的本质：设置边界（发送多少个接受多少个）
import time
import socket
import struct
sk = socket.socket()
sk.connect(('127.0.0.1', 9001))
length = sk.recv(4)
length = struct.unpack('i', length)[0]#因为其返回的是个元组
msg1 = sk.recv(length)
print(msg1.decode('utf-8'))

msg2 = sk.recv(1024)
print(msg2.decode('utf-8'))
sk.close()
