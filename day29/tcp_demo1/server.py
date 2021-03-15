import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9001))# 申请操作系统的资源
sk.listen()
print('sk:',sk)
conn, addr = sk.accept()# conn里存储的是一个客户端和我serve端的连接信息
print(addr) # ('127.0.0.1', 6254)
print('coon:',conn)
conn.send(b'hello')
msg = conn.recv(1024)
print(msg)
conn.close()    # 四次挥手,断开连接

sk.close()    # 关闭服务，归还申请的操作系统资源
