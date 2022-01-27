import ipaddress
import subprocess


def host_ping(lst):
    for address in lst:
        try:
            ipv4_int = ipaddress.ip_address(address)
        except ValueError:
            ipv4_int = address
        args = ['ping', str(ipv4_int)]
        try:
            subprocess.check_call(args, stdout=subprocess.PIPE)
            print(f'{ipv4_int}: Узел доступен')
        except subprocess.CalledProcessError:
            print(f'{ipv4_int}: Узел недоступен')


if __name__ == '__main__':
    addresses = ['10.0.5.10', 'localhost', '192.168.0.1', 'yankjkdex.ru', '80.0.1.15']
    host_ping(addresses)
