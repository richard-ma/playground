#!/usr/bin/env python
# encoding: utf-8

import random
import sys

length = 100
if len(sys.argv) > 1:
    length = int(sys.argv[1])

for i in xrange(0, length):
    start = random.randint(0, 99)
    end = random.randint(start+1, 100)

    print "%d %d" % (start, end)
