#!/usr/bin/env python

import socket
import time

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 80))
    time.sleep(2)
    sock.send("GET /test.html HTTP/1.1\nHOST: localhost:80\n\n")
    print sock.recv(1024)
    sock.close

if __name__ == '__main__':
    main()
