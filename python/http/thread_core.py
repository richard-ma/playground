#!/usr/bin/env python

import threading

class ThreadCore(threading.Thread):
    def __init__(self):
        super(ThreadCore, self).__init__()
        self.connection = None

    def run(self, conn):
        self.connection = conn
