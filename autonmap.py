#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, It's a simple nmap automation tool....")
print("<<-------------------------------------------->>")

ip_addr = input("Enter IP: ") 
print ("IP you've entered is", ip_addr)
type(ip_addr)


resp = input("""\n 1) SYN ACK Scan
                   2) UDP Scan
                   3) Comprehensive Scan\n""")

print("You have selected option", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version)
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo)
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    
    
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version)
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo)
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    
    
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version)
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo)
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    
    
    
elif resp >= '4':
    print("Yu Drunk Broo???")
    
