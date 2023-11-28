import socket as s
ss=s.socket(s.AF_INET,s.SOCK_DGRAM)
ss.bind(("127.0.0.1",1200))
print("===============uppercase serv==========")
while True:
    m,a=ss.recvfrom(1024)
    f=m.upper()
    print(f)
    ss.sendto(f,a)
