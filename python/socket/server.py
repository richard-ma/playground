#!/usr/bin/env python

import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8001))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            print buf
        except socket.timeout:
            print 'timeout'
        connection.close()

if __name__ == '__main__':
    main()
