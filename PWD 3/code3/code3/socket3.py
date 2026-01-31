import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_addr = ('localhost', 80)
sock.connect(('data.pr4e.org', 80))
# sock.connect(client_addr)
print(sock.getsockname())
print(sock.getpeername())
print(type(sock))