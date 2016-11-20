#!/usr/bin/env python

from http_message import HttpMessage
import time

class HttpResponse(HttpMessage):
    def __init__(self):
        super(HttpResponse, self).__init__()
        self.httpVersion = 'HTTP/1.1'
        self.setStatus(500)
        self._header()

    def setStatus(self, code):
        self.statusCode, self.reasonPhrase = self._status(code)

    def setBody(self, body):
        self.body = body
        self.header['Content-Lenght'] = str(len(self.body))

    def _status(self, code):
        if code == 200:
            return (code, 'OK')
        elif code == 404:
            return (code, 'Not Found')
        elif code == 500:
            return (code, 'Internal Server Error')

    def _startLine(self):
        self.startLine = "%s %d %s" % (
                self.httpVersion,
                self.statusCode,
                self.reasonPhrase,
                )

    def _header(self):
        self.header['Server'] = 'cube/0.1'
        self.header['Date'] = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
        self.header['Content-Type'] = 'text/html'
        self.header['Connection'] = 'keep-alive'

    def __str__(self):
        self._startLine()
        return super(HttpResponse, self).__str__()
