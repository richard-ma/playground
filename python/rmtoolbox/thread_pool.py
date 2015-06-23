#!/usr/bin/env python
# encoding: utf-8

################################################################
# from: http://www.handaoliang.com/a/20071102/184706.html
################################################################

import Queue, threading, sys
from threading import Thread

class Worker(Thread):

    """Docstring for Worker. """

    worker_count = 0
    timeout = 1

    def __init__(self, workQueue, resultQueue, **kwds):
        """@todo: to be defined1.

        :workQueue: @todo
        :resultQueue: @todo
        :**kwds: @todo

        """
        Thread.__init__(self, **kwds)

        self.id = Worker.worker_count
        Worker.worker_count += 1

        self.setDaemon(True)

        self.workQueue = workQueue
        self.resultQueue = resultQueue

        self.start()

    def run(self):
        """@todo: Docstring for run.
        :returns: @todo

        """
        while True:
            try:
                callable, args, kwds = self.workQueue.get(timeout = Worker.timeout)
                res = callable(*args, **kwds)
                print "worker[%2d]: %s" % (self.id, str(res))
                self.resultQueue.put(res)
            except Queue.Empty:
                break
            except:
                print "worker[%2d]" % (self.id), sys.exc_info()[:2]
                raise

class WorkerManager():

    """Docstring for WorkerManager. """

    def __init__(self, num_of_workers = 10, timeout = 2):
        """@todo: to be defined1. """

        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.workers = []
        self.timeout = timeout
        self._recruitThreads(num_of_workers)

    def _recruitThreads(self, num_of_workers):
        """@todo: Docstring for _recruitThreads.

        :num_of_workers: @todo
        :returns: @todo

        """

        for i in range(num_of_workers):
            worker = Worker(self.workQueue, self.resultQueue)
            self.workers.append(worker)

    def wait_for_complete(self):
        """@todo: Docstring for wait_for_complete.
        :returns: @todo

        """
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()
            if worker.isAlive() and not self.workQueue.empty():
                self.workers.append(worker)
        print "All jobs are completed."

    def add_job(self, callable, *args, **kwds):
        """@todo: Docstring for add_job.

        :callable: @todo
        :*args: @todo
        :**kwds: @todo
        :returns: @todo

        """
        self.workQueue.put((callable, args, kwds))

    def get_result(self, *args, **kwds):
        """@todo: Docstring for get_result.

        :*args: @todo
        :**kwds: @todo
        :returns: @todo

        """
        return self.resultQueue.get(*args, **kwds)

###############################################
# Test code
###############################################
'''
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

    wm = WorkerManager(5)
    for i in range(15):
        print "adding %d" % i
        wm.add_job(some_work, 'Work %d' % i, randrange(2, 9))
    wm.wait_for_complete()
    print 'end testing'
'''
