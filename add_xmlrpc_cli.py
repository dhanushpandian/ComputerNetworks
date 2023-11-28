import xmlrpc.client
p=xmlrpc.client.ServerProxy(("http://localhost:8000"))

a=int(input("enetr 1st: "))
b=int(input("enetr 2nd: "))
c=[1,2,3,4,5,6]

print(p.add(a,b))
print(p.sub(a,b))
print(p.maxx(c))
