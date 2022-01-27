import ipaddress
import subprocess

import tabulate
from progress.bar import IncrementalBar


def host_range_ping(ip, ip_range, start_ip_range=0):
    subnet = ipaddress.ip_network(ip)
    list_host = subnet.hosts()
    bar = IncrementalBar('Ping', max=ip_range)
    for iter in range(start_ip_range - 1):
        next(list_host)
    list_of_ip = []
    for host in list_host:
        bar.next()
        args = ['ping', str(host)]
        try:
            subprocess.check_call(args, stdout=subprocess.PIPE)
            list_of_ip.append((host.compressed, 'доступен'))
        except subprocess.CalledProcessError:
            list_of_ip.append((host.compressed, 'не доступен'))
        if len(list_of_ip) >= ip_range:
            break
    bar.finish()
    print(tabulate.tabulate(list_of_ip, headers=['ip-адреса', 'статус']))


if __name__ == '__main__':
    host_range_ping('5.255.255.0/24', 5, start_ip_range=74)
