import socket  # corre
extra={}
class tra:
    def __init__(self):
        self.__extra={}
    def getname(self):
        print('getname() called')
        return self.__extra
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_addr = ('localhost', 80)
sock.connect(('data.pr4e.org', 80))
# sock.connect(client_addr)
print(sock.getsockname())
print(sock.getpeername())
p1=tra()
p1.extra=sock.getsockname()
print(type(p1.extra))
# p1.extra['sockname']=sock.getsockname()
print(p1)