import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8081))

msg1 = sk.recv(1024)
print(msg1.decode('utf-8'))
while True:
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    smsg = input('>>>')
    sk.sendto(smsg.encode('utf-8'), addr)
    if smsg.upper() == "Q":break
sk.close()







