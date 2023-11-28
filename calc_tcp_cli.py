from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.connect(("127.0.0.1",8000))
print("======calc cli==========")
while  True:
    m=input("enetr a expression :  ")
    s.send(m.encode('utf-8'))
    d=s.recv(100).decode()
    print("-->",d)
    
