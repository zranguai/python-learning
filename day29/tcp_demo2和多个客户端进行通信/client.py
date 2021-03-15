import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))
while True:  # 和服务器端使劲聊
    msg = sk.recv(1024).decode('utf-8')
    if msg.upper() == 'Q':break#关闭和该服务器通信
    print(msg)
    send_msg = input('>>>')
    sk.send(send_msg.encode('utf-8'))
    if send_msg.upper() == 'Q': break
sk.close()
