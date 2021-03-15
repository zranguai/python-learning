import socket

server = socket.socket()
ip_port = ('127.0.0.1', 8002)
server.bind(ip_port)
server.listen()

while True:
    conn, addr = server.accept()
    from_client_msg = conn.recv(1024)
    print(from_client_msg.decode('utf-8'))
    conn.send(b'HTTP/1.1 200 ok\r\nv1:k1\r\n\r\n')
    # conn.send(b'hello, world')
    with open('helloworld.html', 'rb') as f1:
        content = f1.read()
    conn.send(content)
    conn.close()





