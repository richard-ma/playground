#!/usr/bin/env python

from http_message import HttpMessage

class HttpRequest(HttpMessage):
    def __init__(self, data):
        super(HttpRequest, self).__init__(data)
        (self.method, self.target, self.httpVersion) = self.start_line.split(' ')
