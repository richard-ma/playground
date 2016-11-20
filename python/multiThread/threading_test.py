#!/usr/bin/env python

import threading
import time
import random

class Test(threading.Thread):
    def __init__(self, name):
        super(Test, self).__init__()
        self.name = name

    def run(self):
        print 'thread %s start' % self.name
        time.sleep(random.randint(1, 5))
        print 'thread %s stop' % self.name

if __name__ == "__main__":
    print "start"
    t_list = list()
    for i in xrange(0, 10):
        t_list.append(Test(i))

    for i in xrange(0, 10):
        t_list[i].start()

    for i in xrange(0, 10):
        t_list[i].join()

    print "stop"
