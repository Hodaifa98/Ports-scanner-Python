#Import required modules.
import socket

target = "localhost"

def portScan(port):
    try:
        #AF_INET = Address family used of IPv4.
        #SOCK_STREAM = TCP instead of UDP.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False

print(portScan(80))