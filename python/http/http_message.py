#!/usr/bin/env python

class HttpMessage(object):
    def __init__(self):
        self.startLine = ''
        self.header = dict()
        self.body = ''

    def _parse(self, data):
        lines = data.splitlines()
        self.startLine = lines[0]
        idx = 1
        while lines[idx] != '':
            (k, v) = lines[idx].split(':', 1)
            self.header[k.strip()] = v.strip()
            idx += 1
        idx += 1 # skip CRLF line

        self.body = ''.join(lines[idx:])

    def __str__(self):
        startLine_str = self.startLine
        header_str = "".join([k + ": " + v + "\n" for k, v in self.header.iteritems()])
        body_str = self.body

        return startLine_str + "\n" + header_str + "\n" + body_str
