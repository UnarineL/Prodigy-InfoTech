# Network Packet Analyzer

This Python program is a packet sniffing tool developed for educational purposes. It captures and analyzes network traffic, focusing on TCP packets, and logs key information such as source and destination IP addresses, ports, protocols, and partial payloads. The tool emphasizes ethical use, requiring user consent before it starts capturing packets.

## Features

- **Real-time Packet Sniffing**: Captures TCP packets as they traverse the network, allowing users to monitor live traffic.
- **Detailed Packet Analysis**:
  - **Source and Destination IP addresses**: Identifies where the packet is coming from and where it's going.
  - **Source and Destination Ports**: Provides the specific ports being used for the transmission, which can help identify the type of service (e.g., HTTP, FTP).
  - **Protocol Type**: Displays the protocol being used (e.g., TCP, UDP), providing insights into the nature of the traffic.
  - **Payload**: Shows the first 50 characters of the packet payload, which can contain crucial information for analysis.
- **Output Logging**: Saves the captured packet details to a log file (`packet_sniffer_results.txt`) for later review, making it easy to analyze traffic after the session.
- **Ethical Disclaimer**: Prompts users to accept terms and conditions to ensure responsible usage, reinforcing the importance of ethical practices in network monitoring.

## Prerequisites

- **Python 3.x installed**: Ensure you have Python 3.x set up on your system. You can download it from the [official Python website](https://www.python.org/downloads/).
- **Scapy library installed**: This tool relies on the Scapy library for packet manipulation and analysis. Install it via `pip`:
  ```bash
  pip install scapy

## Usage

**Running the Program**
Start the Program: Run the script to begin the packet sniffing process.

**bash**

python packet_sniffer.py
Disclaimer: The program will display a disclaimer outlining the ethical use of the tool. Read the terms carefully and type y to accept and proceed.

Packet Capture: The program will capture TCP packets and display their details in the console while saving them to the log file.

##Log File Output
Captured packet details are saved to a text file with the following information:

Source IP Address
Destination IP Address
Source Port
Destination Port
Protocol Type
Payload (first 50 characters)
Example log entry:

## yaml

Source IP: 192.168.1.10
Destination IP: 192.168.1.1
Source Port: 443
Destination Port: 56789
Protocol: 6
Payload (partial): GET / HTTP/1.1...
Ethical Use
This tool is intended solely for educational purposes. You are responsible for using this program in compliance with applicable laws and regulations. Use it only on networks and systems where you have permission to do so.

## Disclaimer
By using this tool, you agree to the following:

You will only use this tool on networks and systems for which you have explicit permission.
You will not use this tool to capture sensitive, private, or confidential data.
The author is not responsible for any damages or legal consequences resulting from misuse of this tool.

## Developed By
This packet analyzer was developed during my internship at Prodigy InfoTech, demonstrating my ability to create and analyze network traffic using Python.