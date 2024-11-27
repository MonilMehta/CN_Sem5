import random,time,socket

HOST='127.0.0.1'
PORT=5001
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect((HOST,PORT)) 
TIMEOUT=5
while True:
    message=input("Enter the data here: ")
    ss.sendall(message.encode())
    if message=='end':
        break
    ss.settimeout(TIMEOUT)
    try:
        data=ss.recv(1024)
        print(data.decode())
    except socket.timeout:
        print(f"ACK not received for '{message}', retransmitting...")
        ss.sendall(message.encode())