#Import required modules.
import socket
import threading
from queue import Queue

target = "localhost"
queue = Queue()
open_ports = []
number_of_threads = 500

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

def fillQueueWithList(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print(F"Port: {port} is open.")
            open_ports.append(port)

if __name__ == "__main__":
    port_list = range(1, 3320)
    fillQueueWithList(port_list)

    thread_list = []

    for t in range(number_of_threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        #Wait until the thread is done.
        thread.join()

    print("Open ports are: ", open_ports)