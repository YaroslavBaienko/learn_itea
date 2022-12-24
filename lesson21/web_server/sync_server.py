import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 5000))
server.listen()


while True:
    print('Before .accept()')
    client, client_addr = server.accept()
    print(f'Connection from {client_addr}')

    while True:
        print('Before .recv()')
        request = client.recv(4096)

        if not request:
            client.close()
            break

        response = f'Hello, {client_addr}'.encode()
        client.send(response)

    print('Out of .recv()')

