#!/usr/bin/env python

class HttpMessage(object):
    def __init__(self, data):
        self.start_line = ''
        self.header = dict()
        self.body = ''
        self._parse(data)

    def _parse(self, data):
        lines = data.splitlines()
        self.start_line = lines[0]
        idx = 1
        while lines[idx] != '':
            (k, v) = lines[idx].split(':', 1)
            self.header[k] = v
            idx += 1
        idx += 1 # skip CRLF line

        self.body = ''.join(lines[idx:])
