import socket

ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('localhost',50001))

while True:
    data=input("Enter data (or 'exit' to quit): ")
    if data=='exit':
        break
    ss.send(data.encode())
ss.close()