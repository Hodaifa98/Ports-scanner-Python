#Import required modules.
import socket
import threading
from queue import Queue


#Final global variables.
TARGET = "localhost"
MAX_PORTS = 65535
NUMBER_OF_THREADS = 500
#Global variables.
ports_queue = Queue()
open_ports = []

#fillQueueWithList.
def fillPortsQueueWithList(ports_list):
    for port in ports_list:
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
    print("This program scan for open ports and display their respective service names if available.")
    
    #Read the user input.
    try:
        #Read the starting port.
        print(f"Enter the starting port to scan from (1 <= port < {MAX_PORTS}) or leave empty to start with '1': ")
        from_port = input()
        if str.isdigit(from_port):
            from_port = int(from_port)
            if(from_port < 1 or from_port > MAX_PORTS):
                from_port = 1
        else:
            from_port = 1
        #Read the end port.
        print(f"Enter the end port to scan to (from_port < port <= {MAX_PORTS}) or leave empty to scan until '{MAX_PORTS}': ")
        to_port = input()
        if str.isdigit(to_port):
            to_port = int(to_port)
            if(to_port <= from_port or to_port > MAX_PORTS):
                to_port = MAX_PORTS
        else:
            to_port = MAX_PORTS
    except:
        pass

    #Fill the ports list.
    ports_list = range(from_port, to_port)

    #Fill the ports queue with the port numbers supplied by the user.
    fillPortsQueueWithList(ports_list)

    #Initiate a thread list that we will store all the threads used in this program.
    threads_list = []

    #Loop through the pre-defined number of threads.
    for t in range(NUMBER_OF_THREADS):
        #Initiate a thread that will handle checking for open ports.
        thread = threading.Thread(target=worker)
        threads_list.append(thread)

    #Start all threads.
    for thread in threads_list:
        thread.start()

    #Loop through the threads and wait for them to be finished before the open parts are displayed.
    for thread in threads_list:
        thread.join()

    if len(open_ports) != 0:
        print(f"\nThe open ports from '{from_port}' to '{to_port}' are:\n", open_ports)
    else:
        print(f"\nThere are no open ports from '{from_port}' to '{to_port}'.")