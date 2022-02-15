from socket import *


def send_udp_message(server,message):
    client_socket = socket(AF_INET,SOCK_DGRAM)
    client_socket.sendto(message.encode(),server)
    response, server_address = client_socket.recvfrom(1048)
    return response.decode();


if __name__ == '__main__':
    ip = input('Enter IP address:')
    port = int(input('Enter port: '))
    message = input('Enter message: ')
    print(send_udp_message(('127.0.0.1', 12000), message))
