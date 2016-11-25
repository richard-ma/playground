#!/usr/bin/env python

import sys

class Organism(object):
    def __init__(self, name = 'None'):
        self.name = name
        self.ripeAge = sys.maxint
        self.birth = 0
        self.lifetime = sys.maxint

    def age(self):
        t = global time
        return t - self.birth

    def isRipe(self):
        if self.age() >= self.ripeAge:
            return True
        else:
            return False

    def isDeath(self):
        if self.age() >= self.lifetime:
            return True
        else:
            return False
