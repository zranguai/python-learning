import socket
import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            try:
                content = conn.recv(1024).decode('utf-8')
                print(content)
                conn.send(content.upper().encode('utf-8'))
            except ConnectionResetError:
                break

server = socketserver.ThreadingTCPServer(('127.0.0.1',9001), Myserver)
server.serve_forever()
















