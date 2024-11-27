import socket,time,random

ss=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    packet=random.randint(1,5)
    message=str(packet)
    ss.sendto(message.encode(),('localhost',5001))
    print(f"Sent packet of size {packet}")

    time.sleep(3)
