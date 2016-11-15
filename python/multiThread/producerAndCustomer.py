#!/usr/bin/env python

import threading
import time

class Producer(threading.Thread):
    def __init__(self, t_name):
        threading.Thread.__init__(self, name=t_name)

    def run(self):
        global x
        con.acquire()
        if x > 0:
            con.wait()
        else:
            for i in range(5):
                x+=1
                print "Producing..." + str(x)
            con.notify()
        print x
        con.release()

class Consumer(threading.Thread):
    def __init__(self, t_name):
        threading.Thread.__init__(self, name=t_name)

    def run(self):
        global x
        con.acquire()
        if x == 0:
            print 'customer wait'
            con.wait()
        else:
            for i in range(5):
                x-=1
                print "consuming..." + str(x)
            con.notify()
        print x
        con.release()

con = threading.Condition()

x = 0

print 'start consumer'
c = Consumer('consumer')
print 'start producer'
p = Producer('producer')

p.start()
c.start()
p.join()
c.join()

print x
