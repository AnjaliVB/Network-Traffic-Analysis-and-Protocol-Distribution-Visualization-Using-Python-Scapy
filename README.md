<h1>Network Traffic Analyzer & TCP SYN Packet Generator</h1>

A Python-based networking and cybersecurity project that demonstrates network packet capture, protocol analysis, traffic visualization, and controlled TCP SYN packet generation using Scapy and Matplotlib.

📌 **Project Overview**

This project consists of two Python scripts that demonstrate fundamental concepts of network traffic analysis and packet generation.

The Network Traffic Analyzer captures network packets, classifies them into TCP, UDP, ICMP, and other protocol categories, and visualizes the results using a bar chart.

The TCP SYN Packet Generator creates TCP SYN packets with randomized source ports and sends them to a specified target for controlled network testing and packet-analysis experiments.

Together, these scripts provide a practical introduction to packet-level networking, protocol identification, traffic monitoring, and network security fundamentals.

🎯**Objective**

To capture, analyze, and visualize network traffic while generating controlled TCP SYN packets to understand packet transmission, TCP communication, and basic network monitoring techniques.

✨ **Features**
1. Network Traffic Analyzer
- Network Packet Capture: Captures up to 100 packets using Scapy.
- Protocol Identification: Identifies TCP, UDP, and ICMP traffic.
- Packet Classification: Categorizes unmatched IP packets under an OTHERS category.
- Packet Counting: Maintains separate counters for each protocol category.
- Traffic Visualization: Generates a bar chart using Matplotlib.
- Color-Coded Graph: Uses different colors to distinguish protocol categories.
- Basic Traffic Profiling: Provides a summary of observed network protocol distribution.
2. TCP SYN Packet Generator
- TCP SYN Generation: Constructs TCP packets with the SYN flag set.
- Randomized Source Ports: Selects source ports between 1024 and 65535.
- Destination Port Configuration: Uses port 80 by default.
- Configurable Packet Count: Sets the number of packets to generate.
- Configurable Interval: Defines the delay between packet transmissions.
- Target Configuration: Allows the destination IP address to be specified.
- Packet Transmission: Uses Scapy's send() function to transmit the generated packets.

🛠️ **Technologies Used**

- Python	Core programming language
- Scapy	Packet capture, inspection, construction, and transmission
- Matplotlib	Traffic visualization
- Random source-port selection

⚙️ **Project Workflow**

1. Network Traffic -> Network Traffic Analyzer -> Capture Packets -> Identify IP Protocols -> Count TCP, UDP, ICMP and Others -> Generate Bar Chart

2. Configure Target and Ports -> Create TCP SYN Packets -> Randomize Source Ports -> Transmit Test Packets -> Observe with Analyzer

📦 **Installation**

**Prerequisites**

1. Python 3.9 or a compatible Python version.
2. Scapy.
3. Matplotlib.
4. A network interface or local test environment configured for authorized testing.

**Step 1: Clone the Repository**

    git clone https://github.com/AnjaliVB/Network-Traffic-Analysis-and-Protocol-Distribution-Visualization-Using-Python-Scapy
    cd Network-Traffic-Analysis-and-Protocol-Distribution-Visualization-Using-Python-Scapy

**Step 2: Install Dependencies**

Create a requirements.txt file containing:

scapy

matplotlib

**Install the dependencies:**

python -m pip install -r requirements.txt

**Step 3: Configure the Scripts**

For the TCP SYN generator, configure the destination IP address, destination port, packet count, and transmission interval according to your authorized test environment.

🚀 **Usage**

Running the Network Traffic Analyzer

Run the analyzer:

    python network_analyzer.py


The script captures up to 100 packets, updates the protocol counters, and displays a bar chart of the resulting traffic distribution.

Depending on the operating system and interface configuration, packet capture may require elevated privileges.

Running the TCP SYN Packet Generator

Run the generator only in an authorized laboratory environment:

    python tcp_syn_generator.py


The script constructs TCP SYN packets with randomized source ports and sends them to the configured destination.

_*Safety note: Use a controlled local lab or an explicitly authorized test system. Avoid sending generated traffic to public IP addresses or third-party systems without permission._

📊 **Expected Results**

The analyzer produces a bar chart with four categories:

TCP
UDP
ICMP
OTHERS

<img src="https://github.com/user-attachments/assets/3f76347d-a64f-47f1-9292-75a7ce8b6195" >

The height of each bar represents the number of packets classified into that category during the capture session.

The actual counts depend on the network interface, active applications, available traffic, and capture configuration.


TCP SYN Packet Generator

The generator sends the configured number of TCP SYN packets and prints a completion message after Scapy's send operation returns.

Successful transmission does not necessarily mean the destination received the packets, accepted a connection, or responded. Those outcomes require separate verification.

🔐**Relevance**

This project demonstrates concepts relevant to defensive network security and network troubleshooting.

* Network Monitoring: Observing traffic visible to a network interface.
* Protocol Analysis: Understanding TCP, UDP, ICMP, and IP packet classification.
* Packet-Level Inspection: Learning how packet layers can be inspected and constructed.
* Traffic Profiling: Summarizing observed network traffic by protocol.
* TCP Fundamentals: Exploring SYN flags, source ports, and destination ports.
* Security Testing Fundamentals: Understanding how controlled packet generation can support laboratory testing.
* Data Visualization: Presenting packet statistics in a readable graphical format.

TCP SYN packets are used during normal TCP connection establishment. SYN generation can also be relevant to SYN-flood testing, but this project does not independently detect or mitigate such attacks.

🎓 **Outcome & Learnings**

Gained practical experience in network packet capture, protocol identification, TCP packet construction, and traffic visualization using Python, Scapy, and Matplotlib. Developed a foundational understanding of packet transmission, protocol distribution, and network security monitoring.

📌 **Limitations**

- The analyzer processes a limited sample of 100 packets by default.
- The graph is generated after capture finishes rather than continuously updated.
- Protocol counts alone cannot establish whether traffic is malicious.
- The analyzer does not currently inspect payloads, track TCP connections, or generate security alerts.
- The TCP SYN generator does not verify delivery or analyze responses.
- Loopback packets may not be visible on other network interfaces.
