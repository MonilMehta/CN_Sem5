import socket, time

bucket_size = 10
current_level = 0

def leak_packets():
    global current_level
    leak_amount=2
    if current_level>0:
        current_level-=leak_amount
        print(f"Leaked {leak_amount} packets. Current level: {current_level}")
    else:
        print("No packets to leak.")

ss=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ss.bind(('localhost',5001))

while True:
    data,addr=ss.recvfrom(1024)
    packet=int(data.decode())

    if current_level+packet<=bucket_size:
        current_level+=packet
        print(f"Received packet of size {packet}. Current level: {current_level}")
    else:
        print(f"Bucket overflow! Dropped packet of size {packet}")
    
    leak_packets()
    time.sleep(2)