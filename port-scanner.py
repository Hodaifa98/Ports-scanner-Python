#Import required modules.
import socket
import threading
from queue import Queue


#Final global variables.
TARGET = "localhost"
MAX_NUMBER_PORTS = 65535
NUMBER_OF_THREADS = 500
#Global variables.
ports_queue = Queue()
open_ports = []

#fillQueueWithList.
def fillPortsQueueWithList(port_list):
    for port in port_list:
        ports_queue.put(port)

#portScan.
def portScan(port):
    try:
        #Initiate a socket.
        #AF_INET = Address family used for IPv4.
        #SOCK_STREAM = A TCP socket.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Try connecting to a target host with the port number supplied as an argument.
        s.connect((TARGET, port))
        #Return true if there was no exception, meaning the port is open.
        return True
    #If a socket couldn't connect, then an exception will be thrown, meaning that the port wasn't open.
    except:
        return False

#worker.
def worker():
    while not ports_queue.empty():
        #Get the next port from the Queue after removing it.
        port = ports_queue.get()
        #If the port is open.
        if portScan(port):
            #Try getting the service name associated with the port, otherwise, an exception is thrown.
            try:
                port_name = socket.getservbyport(port)
            except:
                port_name = "UNKNOWN"
            #Display the open port, and its service name.
            print(F"Port: {port} is open - Service: {port_name}.")
            open_ports.append(port)


#main.
if __name__ == "__main__":
    port_list = range(1, 5000)
    fillPortsQueueWithList(port_list)

    #Initiate a thread list that we will store all the threads used in this program.
    thread_list = []

    #Loop through the pre-defined number of threads.
    for t in range(NUMBER_OF_THREADS):
        #Initiate a thread that will handle checking for open ports.
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    #Start all threads.
    for thread in thread_list:
        thread.start()

    #Loop through the threads and wait for them to be finished before the open parts are displayed.
    for thread in thread_list:
        thread.join()

    print("\nThe open ports are: ", open_ports)