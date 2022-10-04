from urllib.request import urlopen
import json
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1', 2000))
#
# server.listen(4)
# print('Working...')
# client_socket, address = server.accept()
# data = client_socket.recv(1024).decode('utf-8')
# print(data)
# content = "Russian warship go fuck yourself!".encode('utf-8')
# client_socket.send(content)
# print('Shutdown')


url = "https://google.ru"
with urlopen(url) as response:
    body = response.read()
   #  print(todo_item)
    print(response.headers)
