from scapy.all import IP, ICMP, TCP, UDP, Raw, send
import random
import time

packet_count = 50	#defining no. of packets to be sent
interval = 1		#wait for 1 sec each after packet sent
target_ip = "127.0.0.0" #sending packets on localhost


'''
	defining a function to send tcp syn packets
'''
def send_tcp_syn():
    # send tcp syn packets
    packet = IP(dst=target_ip) / TCP(
        sport=random.randint(1024, 65535),
        dport=80,
        flags="S"
    )
	#sport is sender's port
	#dport is destination port

    send(packet, count=packet_count, interval=interval)	#send() will send the specified no. of packets 
    print("tcp packets sent")

send_tcp_syn()
