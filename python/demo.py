#!/usr/bin/env python
# encoding: utf-8

from rmtoolbox.ThreadManager import ThreadManager

def some_work(work_name, sleep_time):
   """@todo: Docstring for some_work.

   :arg1: @todo
   :returns: @todo

   """
   time.sleep(sleep_time)
   return "%s completed. Working %d second(s)." % (work_name, sleep_time)

if __name__ == '__main__':
    import time
    from random import randrange

    wm = ThreadManager(5)
    for i in range(15):
        print "adding %d" % i
        wm.add_job(some_work, 'Work %d' % i, randrange(2, 9))
    wm.wait_for_complete()
    print 'end testing'
