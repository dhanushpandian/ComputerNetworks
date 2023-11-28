#CLIENT SIDE:
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    print("Enter the Word")
    w=input("-->",)
    m=str.encode(w)
    addr = ("127.0.0.1", 12000)
    client_socket.sendto(m,addr)
    data,server = client_socket.recvfrom(1024)
    print("Meaning is %s",data)