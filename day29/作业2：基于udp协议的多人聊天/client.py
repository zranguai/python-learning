import socket
sk = socket.socket(type=socket.SOCK_DGRAM)

qq_name_dic = {    # 聊天对象列表
    'apple': ('127.0.0.1', 8081),
    'orange': ('127.0.0.1', 8081),
    'egg': ('127.0.0.1', 8081),
    'yuan': ('127.0.0.1', 8081),
}

# serve = ('127.0.0.1', 9001)

while True:
    print(qq_name_dic)
    serve = input('请输入你要聊天的对象>>>')
    info = f'本次聊天对象为{serve}'
    sk.sendto(info.encode('utf-8'),qq_name_dic[serve])
    while True:
        cmsg = input('你要发送的消息，输入q退出本次聊天>>>')
        if cmsg.upper() == 'Q': break
        sk.sendto(cmsg.encode('utf-8'), qq_name_dic[serve])

        msg = sk.recv(1024).decode('utf-8')
        if msg.upper() == 'Q':break
        print(msg)    # 你接受的消息









