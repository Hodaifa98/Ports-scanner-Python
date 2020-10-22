#Import required modules.
import socket
import threading
from queue import Queue

target = "localhost"
queue = Queue()
open_ports = []

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

def fill_queue_with_range(from_port, to_port):
    for port in range(from_port, to_port):
        queue.put(port)

def fill_queue_with_list(port_list):
    for port in port_list:
        queue.put(port)

