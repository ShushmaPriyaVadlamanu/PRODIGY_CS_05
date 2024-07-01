from scapy.all import *

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        payload = packet[IP].payload

        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {proto}")
        print(f"Payload: {payload}")

def start_packet_sniffer():
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    print("Starting Network Packet Analyzer...")
    start_packet_sniffer()
