import time
import random

window_size = 4

total_frames = 10
sent_frames = 0

ack_received = [False] * total_frames
ack_waiting=[]

while False in ack_received:
    while sent_frames < total_frames and len(ack_waiting) < window_size:
        print(f'Sending frame {sent_frames}')
        ack_waiting.append(sent_frames)
        sent_frames+=1
        time.sleep(1)
    
    for i in ack_waiting:
        ack = random.choice([True, False])
        if ack:
            print(f'ACK received for frame {i}')
            ack_received[i] = True
            ack_waiting.remove(i)
        else:
            print(f'ACK lost for frame {i}, resending it')
            time.sleep(1)

