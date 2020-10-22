# A multi-threaded, fast ports scanner in Python

This program can be used to find and expose open ports, which can help debug an issue or secure a network, server, computer...

It scans both TCP and UDP ports, and uses multi-threading to quickly scan over the ports specificed by the user. The user can beging scaning from port "1" ("0" is reserved) up until "65535" (maximum number a port can have - highest number that can be represented by 16-bit/2-byte).

This program is multi-threaded because that way it can scan a large number of ports in a short period, and it uses the Queue data type to store ports because it's the preferred way to communicate data between threads.


## Usage:
```python ports-scanner.py```
