### Nmap Automation Tool

## Introduction

This Python script serves as a simple automation tool for Nmap, a powerful network scanning utility. It allows users to perform various types of scans on specified IP addresses.

## Installation

Ensure you have Python 3 installed on your system. You also need to install the python3-nmap package, which can be done using pip:

    pip install python3-nmap

## Usage

1. Run the script using Python 3:
   
       python3 nmap_automation.py

Follow the prompts to enter the target IP address and select the scan type:
- SYN ACK Scan
- UDP Scan
- Comprehensive Scan

## Scan Types
# 1. SYN ACK Scan
This scan type uses the SYN flag to initiate a connection with target ports. It is stealthier than a full connect scan and can be useful for quickly identifying open ports.

# 2. UDP Scan
This scan type sends UDP packets to target ports and waits for responses. It is useful for scanning services that run over UDP, such as DNS and DHCP.

# 3. Comprehensive Scan
This scan type combines various scan options (-sS, -sV, -sC, -A, -O) to provide detailed information about the target system, including open ports, service versions, OS detection, and more.

### Example Usage
    Welcome, It's a simple nmap automation tool....
    <<-------------------------------------------->>
    Enter IP: 192.168.1.1
    IP you've entered is 192.168.1.1
    
      1) SYN ACK Scan
      2) UDP Scan
      3) Comprehensive Scan

After selecting the desired scan type, the script will display the Nmap version, scan information, IP status, protocols detected, and open ports.

## Note
- Ensure you have the necessary permissions to run Nmap scans on target IP addresses.
- Use this tool responsibly and only on networks/systems you have permission to scan.
