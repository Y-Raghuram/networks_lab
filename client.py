import socket
import sys

s = socket.socket()
host = socket.gethostname()
port = 12349
message="client.py"
s.connect((host,port))
print(s.recv(1024))
s.send(message.encode())
f= open("received.txt","w+")
f.write(s.recv(1024).decode())
s.close()
