import socket

# type=socket.SOCK_DGRAM ：udp协议   默认是tcp协议
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9001))
while True:
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    mmsg = input('>>>')
    sk.sendto(mmsg.encode('utf-8'), addr)



# 作业：利用udp进行多人聊天
# 需求：和你的同卓进行聊天并用不同颜色进行标记

# 进阶需求：利用中间的服务器进行你与多人聊天









