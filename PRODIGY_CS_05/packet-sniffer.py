import os
import sys
from scapy.all import *

# Display terms of use disclaimer
print("------------------ Network Packet Sniffer Disclaimer ------------------")
print("This tool is designed for educational and ethical purposes only.")
print("Unauthorized usage, distribution, or modification is strictly forbidden.")
print("By proceeding, you agree to the following conditions:")
print("\n1. You will only use this tool on networks for which you have legal permission.")
print("2. You agree to follow all applicable laws, regulations, and terms of service.")
print("3. You will not use this tool to cause harm or exploit any networks or systems.")
print("4. You will not use this tool to capture or store sensitive or private information.")
print("5. Redistribution or commercialization of this tool is not permitted without consent.")
print("6. The developer is not liable for any damage caused by misuse of this tool.")
print("7. Respect the privacy and security of all networks you interact with using this tool.")

# Check if the user accepts the terms
user_consent = input("\nDo you accept these terms and conditions? (y/n): ")

if user_consent.lower() != 'y':
    print("You must accept the terms to proceed with this tool.")
    sys.exit()

print("\n---------------- Packet Sniffer in Operation ----------------")

# Define the function to handle packet sniffing and logging
def capture_packet(packet):
    if packet.haslayer(TCP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport
        protocol_type = packet[IP].proto
        packet_payload = str(packet[TCP].payload)

        # Build a string to summarize the packet
        log_entry = f"Source IP: {source_ip}\n"
        log_entry += f"Destination IP: {destination_ip}\n"
        log_entry += f"Source Port: {source_port}\n"
        log_entry += f"Destination Port: {destination_port}\n"
        log_entry += f"Protocol: {protocol_type}\n"
        log_entry += f"Payload (partial): {packet_payload[:50]}...\n"

        print(log_entry, end='')
        
        # Append packet information to the log file
        with open(output_log_file, 'a') as log_file:
            log_file.write(log_entry)

# Specify the output file to log sniffed packets
output_log_file = "network_sniffer_output.txt"

# Start sniffing TCP packets and save the results
sniff(filter="tcp", prn=capture_packet, store=0, count=10)

# Confirm log file storage location to the user
print(f"\nCaptured packet details saved to: {output_log_file}")
