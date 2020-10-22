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
    #If a socket couldn't connect, then an exception will be thrown, meaning that the port wasn't open.
    except:
        return False

for port in range(1, 1024):
    is_open = portScan(port)
    if is_open:
        print("Port: {} is open.".format(port))
    else:
        print("Port: {} is closed.".format(port))