#!/usr/bin/env python

import socket
import time

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    time.sleep(2)
    sock.send('1')
    print sock.recv(1024)
    sock.close

if __name__ == '__main__':
    main()
