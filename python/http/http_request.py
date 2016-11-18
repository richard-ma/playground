#!/usr/bin/env python

from http_message import HttpMessage

class HttpRequest(HttpMessage):
    def __init__(self, data):
        super(HttpRequest, self).__init__()
        super(HttpRequest, self)._parse(data)

        (self.method, self.target, self.httpVersion) = self.startLine.split(' ')
