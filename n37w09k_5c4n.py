import scapy.all as scapy
import socket
import random

# 1. Scanarea rețelei pentru IP-uri active
def scan_network(network):
    arp_request = scapy.ARP(pdst=network)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    ip_list = []
    for element in answered_list:
        ip_list.append(element[1].psrc)
    return ip_list

# 2. Salvarea IP-urilor active într-un fișier
def save_ips_to_file(ip_list, filename):
    with open(filename, 'w') as file:
        for ip in ip_list:
            file.write(ip + "\n")

# 3. Sortarea IP-urilor și eliminarea duplicatelor
def sort_and_deduplicate_ips(filename):
    with open(filename, 'r') as file:
        ips = file.readlines()
    
    ips = list(set(ips))  # Eliminarea duplicatelor
    ips.sort()  # Sortare
    return ips

# 4. Amestecarea IP-urilor folosind un algoritm Fibonacci
def fibonacci_shuffle(ips):
    fib_sequence = [0, 1]
    while len(fib_sequence) < len(ips):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    shuffled_ips = []
    for i in fib_sequence:
        if i < len(ips):
            shuffled_ips.append(ips[i])
    
    return shuffled_ips

# 5. Scanarea IP-urilor pentru serviciul SSH
def check_ssh_service(ip_list, ports):
    ssh_ips = []
    for ip in ip_list:
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip.strip(), port))
                if result == 0:
                    banner = sock.recv(1024).decode('utf-8').strip()
                    ssh_ips.append((ip.strip(), port, banner))
                sock.close()
            except Exception as e:
                pass
    return ssh_ips

# 6. Salvarea bannerelor SSH într-un fișier
def save_ssh_output(ssh_ips, output_filename):
    with open(output_filename, 'w') as file:
        for ip, port, banner in ssh_ips:
            file.write(f"IP: {ip}, Port: {port}, Banner: {banner}\n")

if __name__ == "__main__":
    # Exemplu de rețea
    network = "192.168.1.0/24"
    
    # Pasul 1: Scanare rețea
    ip_list = scan_network(network)
    
    # Pasul 2: Salvare IP-uri într-un fișier
    save_ips_to_file(ip_list, "ips_alive.txt")
    
    # Pasul 3: Sortare și eliminare duplicate
    sorted_ips = sort_and_deduplicate_ips("ips_alive.txt")
    
    # Pasul 4: Amestecare IP-uri
    shuffled_ips = fibonacci_shuffle(sorted_ips)
    
    # Pasul 5: Scanare SSH
    ssh_ports = [22, 2222]  # Exemplu de porturi SSH
    ssh_ips = check_ssh_service(shuffled_ips, ssh_ports)
    
    # Pasul 6: Salvare output SSH
    save_ssh_output(ssh_ips, "ssh_output.txt")
