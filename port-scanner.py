#Import required modules.
import socket
import threading
from queue import Queue

TARGET = "localhost"
MAX_NUMBER_PORTS = 65535
NUMBER_OF_THREADS = 500

queue = Queue()
open_ports = []

def portScan(port):
    try:
        #AF_INET = Address family used of IPv4.
        #SOCK_STREAM = TCP instead of UDP.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET, port))
        return True
    #If a socket couldn't connect, then an exception will be thrown, meaning that the port wasn't open.
    except:
        return False

def fillQueueWithList(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            try:
                port_name = socket.getservbyport(port)
            except:
                port_name = "UNKNOWN"
            print(F"Port: {port} is open. Service: {port_name}.")
            open_ports.append(port)

if __name__ == "__main__":
    port_list = range(1, 5000)
    fillQueueWithList(port_list)

    thread_list = []

    for t in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        #Wait until the thread is done.
        thread.join()

    print("Open ports are: ", open_ports)