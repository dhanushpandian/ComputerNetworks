from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",8000))
s.listen(5)
print("===============calc serv================")
c,a=s.accept()
while True:
    data=c.recv(100).decode()
    d=str(data)
    d=eval(d)
    c.send(str(d).encode('utf-8'))