#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, It's a simple nmap automation tool....")
print("<<-------------------------------------------->>")

ipadd = input 
print ("IP you've entered is", ipadd)
type(ipadd)


resp = input  ("""
               1) SYN ACK Scan
               2) UDP Scan
               3) Comprehensive Scan""")
print("You have selected option", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version)
    scanner.scan(ipadd, '1-1024', '-v -sS')
    print(scanner.scaninfo)
    print("IP Status: ", scanner[ipadd].state())
    print(scanner[ipadd].all_protocols())
    print("Open Ports: ", scanner[ipadd]['tcp'].keys())
    
    
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version)
    scanner.scan(ipadd, '1-1024', '-v -sU')
    print(scanner.scaninfo)
    print("IP Status: ", scanner[ipadd].state())
    print(scanner[ipadd].all_protocols())
    print("Open Ports: ", scanner[ipadd]['tcp'].keys())
    
    
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version)
    scanner.scan(ipadd, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo)
    print("IP Status: ", scanner[ipadd].state())
    print(scanner[ipadd].all_protocols())
    print("Open Ports: ", scanner[ipadd]['tcp'].keys())
    
    
    
elif resp >= '4':
    print("Yu Drunk Broo???")
    