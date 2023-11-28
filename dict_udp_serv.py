#SERVER SIDE:
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr=('127.0.0.1', 12000)
server_socket.bind(addr)
while True:
    m,address = server_socket.recvfrom(1024)
    n=m.decode()
    a={'use':'utilize','destroy':'demolish','fall':'drop','decide':'choose','help':'serve','plan':'blueprint', 'show':'display','break':'smash','make':'create','hurry':'rush'}
    g=a[n]
    server_socket.sendto(g.encode(),address)

