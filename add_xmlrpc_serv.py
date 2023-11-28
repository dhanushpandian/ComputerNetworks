from xmlrpc.server import SimpleXMLRPCServer

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def maxx(c):
    return max(c)

s=SimpleXMLRPCServer(("localhost",8000))
print("listening port 8000")

s.register_function(add,"add")
s.register_function(sub,"sub")
s.register_function(maxx,"maxx")

s.serve_forever()
