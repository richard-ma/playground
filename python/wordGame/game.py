#!/usr/bin/env python

from actor import Actor

import constant

class Game(object):
    def __init__(self):
        self.boy = Actor('boy', maxDamage = 10, maxDefance = 5)
        self.girl = Actor('girl', maxDamage = 5, maxDefance = 10)

    def start(self):
        while self.boy.isAlive() and self.girl.isAlive():
            print '%s:%d/%s:%d' % (self.boy.name, self.boy.hp, self.girl.name, self.girl.hp)
            self.boy.attack(self.girl)
            self.girl.attack(self.boy)

        if self.boy.isAlive():
            print '%s Win' % (self.boy.name)

        if self.girl.isAlive():
            print '%s Win' % (self.girl.name)

if __name__ == '__main__':
    counter = 10
    while counter >= 0:
        g = Game()
        g.start()
        counter -= 1
