#!/usr/bin/env python

import socket
import os
import threading

from http_request import HttpRequest
from http_response import HttpResponse

class CoreServer(threading.Thread):

    def __init__(self):
        super(CoreServer, self).__init__()

        self.address = 'localhost'
        self.port = 8001
        self.htmlRoot = '/var/www/html'
        self.index_filename_list = [
                'index.html',
                'index.htm',
                ]

    def _resource_exists(self, target):

        t = os.path.join(self.htmlRoot, target[1:])

        if os.path.isfile(t):
            return t
        elif t[-1] == '/':
            for index_filename in self.index_filename_list:
                t = os.path.join(t, index_filename)
                if os.path.exists(t):
                    return t
        else:
            return False

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.address, self.port))
        sock.listen(5)

        connection, address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            req = HttpRequest(buf)
            res = HttpResponse()

            if self._resource_exists(req.target) != False:
                target = self._resource_exists(req.target)
                if DEBUG:
                    print target
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
    server.join()
