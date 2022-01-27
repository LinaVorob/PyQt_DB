import subprocess


def clients_write_listen(port, ip, amount_client):
    args = ['python', 'D:\PyCharm\ClientServerLessons\project\client.py', '-p', port, '-a', ip]
    for client in range(amount_client):
        subprocess.run(args, stdout=subprocess.PIPE, shell=True)


if __name__ == '__main__':
    num_client = int(input('Количество клиентов: '))
    clients_write_listen('8888', '127.0.0.1', num_client)

