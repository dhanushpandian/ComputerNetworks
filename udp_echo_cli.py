import socket as s
cs=s.socket(s.AF_INET,s.SOCK_DGRAM)
m="HI DHANUSH"
addr=("127.0.0.1",1200)
cs.sendto(m.encode('utf-8'),addr)
d,s=cs.recvfrom(1024)
m=d.decode()
print(m)