import socket as s
cs=s.socket(s.AF_INET,s.SOCK_DGRAM)
print("====================uppercase client=====")
while True:
    m=input("-->")
    a=("127.0.0.1",1200)
    cs.sendto(m.encode('utf-8'),a)
    d,s=cs.recvfrom(1024)
    print("<--",d.decode())
