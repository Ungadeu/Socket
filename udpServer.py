import os
import re
from socket import *


def get_ip(ifaces=['wlan1', 'eth0', 'wlan0']):
    if isinstance(ifaces, str):
        ifaces = [ifaces]
    for iface in list(ifaces):
        search_str = f'ifconfig {iface}'
        result = os.popen(search_str).read()
        com = re.compile(r'(?<=inet )(.*)(?= netmask)', re.M)
        ipv4 = re.search(com, result)
        if ipv4:
            ipv4 = ipv4.groups()[0]
            return ipv4
    return ''


server_port = 12000
server_ip = get_ip('lo0')
print(server_ip,server_port)

if __name__ == "__main__":
    server_socket = socket(AF_INET,SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))
    print(f"The server is ready on ({server_ip}, {server_port}).")
    while True:
        message,client_address = server_socket.recvfrom(1024)
        print(f'MESSAGE RECEIVED FROM {client_address}:'+message.decode())
        modified_message = message.decode().upper()
        server_socket.sendto(modified_message.encode(),client_address)

