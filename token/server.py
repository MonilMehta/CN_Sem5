import socket,time,threading

bucket_token_list = []
MAX_BUCKET_SIZE = 10
TIME_LAPSE = 3
lock = threading.Lock()

def create_server_socket():
    ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.bind(('localhost',50001))
    ss.listen(5)
    print("Server started on localhost:50001")
    return ss

def add_token_to_bucket():
    while True:
        with lock:
            if len(bucket_token_list) < MAX_BUCKET_SIZE:
                bucket_token_list.append(1)
        time.sleep(TIME_LAPSE)

def handle_client(cs):
    while True:
        data=cs.recv(1024).decode()
        if not data:
            continue
        print(f"Received: {data}")
        with lock:
            if bucket_token_list:
                bucket_token_list.pop(0)
                print(f"Token used, bucket: {bucket_token_list}")
            else:
                cs.send("Token not available, wait.".encode())
                print("No token available")
    cs.close()

def start_server():
    ss=create_server_socket()
    threading.Thread(target=add_token_to_bucket,daemon=True).start()
    while True:
        cs,addr=ss.accept()
        print(f"Connection from {addr}")
        threading.Thread(target=handle_client,args=(cs,),daemon=True).start()

start_server()