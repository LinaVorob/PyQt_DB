import ipaddress
import subprocess

import tabulate
from progress.bar import IncrementalBar


def host_range_ping_tab(ip, ip_range, start_ip_range=0):
    subnet = ipaddress.ip_network(ip)
    list_host = subnet.hosts()
    bar = IncrementalBar('Ping', max=ip_range)
    for iter in range(start_ip_range - 1):
        next(list_host)
    list_reachable = []
    list_unreachable = []
    num = 0
    for host in list_host:
        bar.next()
        args = ['ping', str(host)]
        try:
            subprocess.check_call(args, stdout=subprocess.PIPE)
            list_reachable.append(host.compressed)
        except subprocess.CalledProcessError:
            list_unreachable.append(host.compressed)
        num += 1
        if num == ip_range:
            break
    bar.finish()

    list_of_ip = eq_list(list_reachable, list_unreachable)
    print(tabulate.tabulate(list_of_ip, headers=['Reachable', 'Unreachable']))


def eq_list(lst_f, lst_s):
    list_of_ip = []
    min_lst = lst_f if lst_f <= lst_s else lst_s
    for step in range(abs(len(lst_f) - len(lst_s))):
        min_lst.append('-')
    for step in range(max(len(lst_f), len(lst_s))):
        list_of_ip.append((lst_f[step], lst_s[step]))

    return list_of_ip


if __name__ == '__main__':
    host_range_ping_tab('10.0.0.0/24', 4)
