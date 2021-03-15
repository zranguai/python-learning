import socket
sk = socket.socket(type=socket.SOCK_DGRAM)

serve = ('127.0.0.1', 9001)
while True:
    mmmsg = input('>><')
    if mmmsg.upper() == 'Q':break
    sk.sendto(mmmsg.encode('utf-8'), serve)

    msg = sk.recv(1024).decode('utf-8')
    if msg.upper() == 'Q': break
    print(msg)


