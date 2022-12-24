import socket

sock = socket.socket()
sock.connect(('localhost', 5000))
sock.send('hello, server!'.encode())

data = sock.recv(4096)
sock.close()

print(data.decode())

