import scapy.all as scapy
import socket

def get_device_name(ip):
    """Get the device name from its IP address using reverse DNS lookup."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Unknown"

def scan_network(network):
    """Scan the network to find connected devices using Layer 3."""
    print("{:<20} {:<20} {:<}".format("IP Address", "MAC Address", "Device Name"))
    print("-" * 60)
    
    try:
        arp_request = scapy.ARP(pdst=network)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        
        scapy.conf.L3socket = scapy.layers.l3.IP  
        
        answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
        
        for element in answered_list:
            ip = element[1].psrc
            mac = element[1].hwsrc
            device_name = get_device_name(ip)
            print("{:<20} {:<20} {:<}".format(ip, mac, device_name))
    except Exception as e:
        print("Error occurred during network scan:", e)

network_range = "192.168.1.0/24"
scan_network(network_range)
