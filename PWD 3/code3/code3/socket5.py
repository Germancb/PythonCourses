import socket  # corre
class tra:
    def __init__(self):
        self.__extra={}
    def setname(self, extra):
        print('setname() called')
        self.__extra=extra
           
    def getname(self):
        print('getname() called')
        return self.__extra
    extra=property(getname,  setname)
    
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_addr = ('localhost', 80)
sock.connect(('data.pr4e.org', 80))
# sock.connect(client_addr)
p1=tra()
p1.extra={'sockname': sock.getsockname(),'peername': sock.getpeername()}
p1.extra
#p1.extra={'sockname': sock.getsockname()}
# p1.extra={'peername': sock.getpeername()}
print(p1)

for cl, v in p1.extra.items():
    print(cl,v)
