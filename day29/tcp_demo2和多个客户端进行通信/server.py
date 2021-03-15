import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 9001))# 申请操作系统的资源
sk.listen()

while True: # 为了和多个客户端进行握手
    conn, addr = sk.accept()# 能够和多个客户端握手了
    while True: # 和一个客户使劲聊天
        send_msg = input('>>>')
        conn.send(send_msg.encode('utf-8'))
        if send_msg.upper() == 'Q':break#关闭和该用户通信
        msg = conn.recv(1024).decode('utf-8')
        if msg.upper() == 'Q': break
        print(msg)
    conn.close()    # 挥手,断开连接


sk.close()    # 关闭服务，归还申请的操作系统资源



# 今日作业：基于tcp协议的文件传输（发送小的文件/大的文件（包括视频））









