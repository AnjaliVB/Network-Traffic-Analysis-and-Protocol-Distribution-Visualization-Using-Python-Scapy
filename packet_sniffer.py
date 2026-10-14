from scapy.all import sniff, TCP, UDP, ICMP, IP
import matplotlib.pyplot as plt


protocol_counts = {"TCP":0,"UDP":0,"ICMP":0,"OTHERS":0}

#Packet handler function to analyse protcols

def packet_handler(packet):
    if IP in packet:
	#check for tcp
	if TCP in packet:
		protocol_counts["TCP"] += 1
    	elif packet.haslayer(UDP):
        	protocol_counts["UDP"] += 1
    	elif packet.haslayer(ICMP):
        	protocol_counts["ICMP"] += 1
    	else:
        	protocol_counts["OTHERS"] += 1

#capture 100 packets
    sniff(count=100, prn=packet_handler)
   
    # Generate bar chart and plot distribution of protocols
    protocols = list(protocol_counts.keys())
    counts = list(protocol_counts.values())

    plt.bar(protocols, counts, color=['blue','orange','green','red'])
    plt.xlabel("Protocol")
    plt.ylabel("Packet Count")
    plt.title("Distribution of Protocols (TCP, UDP, ICMP, Others)")
    plt.show()
