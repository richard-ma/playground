#!/usr/bin/env python

import socket

from http_request import HttpRequest
from http_response import HttpResponse

class CoreServer(object):

    address = 'localhost'
    port = 8001

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.address, self.port))
        sock.listen(5)

        while True:
            connection, address = sock.accept()
            try:
                connection.settimeout(5)
                buf = connection.recv(1024)
                if DEBUG:
                    req = HttpRequest(buf)
                    res = HttpResponse()
                    print req
                    print res
                else:
                    pass
            except socket.timeout:
                print 'timeout'
            finally:
                connection.close()

if __name__ == '__main__':
    DEBUG = True # set debug mode

    server = CoreServer()
    server.start()
