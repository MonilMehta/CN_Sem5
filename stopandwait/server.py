import random,time,socket

HOST='127.0.0.1'
PORT=5001
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind((HOST,PORT))
ss.listen()

print(f"Server is listening on {HOST}:{PORT}")
conn,address=ss.accept()
print(f"Connected by {address}")

def generate_ack(conn):
    data=conn.recv(1024)
    if not data:
        return
    received_data=data.decode()
    time.sleep(2)
    print(f"The data which is received is: {received_data}")

    if received_data=='end':
        return

    if random.random()<0.3:
        print(f"Simulating lost ACK for: {received_data}")
        return
    ack=f'ACK for: {received_data}'
    conn.sendall(ack.encode())
    conn.close()
generate_ack(conn)
ss.close()