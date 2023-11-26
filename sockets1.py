import socket
print(socket.gethostname())
host=socket.gethostname()
print(socket.gethostbyname(host))
remote="www.github.com"
print(socket.gethostbyname(remote))

ip=socket.gethostbyname(host)
print(socket.inet_aton(ip))

# for port in ['80','25']:
#     serp=socket.getservbyname('tcp',port)
#     print(serp)

