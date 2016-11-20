#!/usr/bin/env python

import socket
import os

from http_request import HttpRequest
from http_response import HttpResponse

class CoreServer(object):

    def __init__(self):
        self.address = 'localhost'
        self.port = 8001
        self.htmlRoot = '/var/www/html'

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.address, self.port))
        sock.listen(5)

        connection, address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            req = HttpRequest(buf)
            res = HttpResponse()

            target = os.path.join(self.htmlRoot, req.target[1:])
            if DEBUG:
                print self.htmlRoot
                print target
            if os.path.exists(target):
                with open(target, 'r') as f:
                    res.setBody(f.read())
                res.setStatus(200)
            else:
                res.setStatus(404)

            connection.send(res.__str__())
            if DEBUG:
                print req
                print res
        except socket.timeout:
            print 'timeout'
        finally:
            connection.close()
        sock.close()

if __name__ == '__main__':
    DEBUG = True # set debug mode

    server = CoreServer()
    server.start()
