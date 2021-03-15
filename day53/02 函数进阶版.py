import socket

server = socket.socket()
ip_port = ('127.0.0.1', 8003)
server.bind(ip_port)
server.listen()

while True:
    conn, addr = server.accept()
    from_client_msg = conn.recv(1024)
    recc = from_client_msg.decode('utf-8')
    # print(from_client_msg.decode('utf-8'))
    print(recc.split('\r\n')[0].split(' ')[1])
    conn.send(b'HTTP/1.1 200 ok\r\nk1:v1\r\n\r\n')
    with open('02hello.html', 'rb') as f1:
        content = f1.read()
    conn.send(content)
    conn.close()





