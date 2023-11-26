from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.connect(("127.0.0.1",8000))
print("================================================clientside===============================================")
while True:
    m=input("--->",)
    s.send(m.encode('utf-8'))
    d=s.recv(100).decode()
    print("<---",d)
    if d=="bye":
        print("end end")
        break
