import socket as s
ss=s.socket(s.AF_INET,s.SOCK_DGRAM)
ss.bind(("",1200))
while True:
    m,a=ss.recvfrom(1024)
    n=m.decode()
    print(n)
    ss.sendto(n.encode('utf-8'),a)
    
