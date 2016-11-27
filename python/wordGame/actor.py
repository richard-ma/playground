#!/usr/bin/env python

import random

import constant

class Actor(object):
    def __init__(self, name, hp = 100, maxDamage = 10, maxDefance = 0):
        self.name = name
        self.hp = hp
        self.maxDamage = maxDamage
        self.maxDefance = maxDefance

    def damage(self):
        return random.randint(0, self.maxDamage)

    def defance(self):
        return random.randint(0, self.maxDefance)

    def isAlive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def beAttacked(self, damage):
        d = damage - self.damage()
        if d < 0:
            d = 0
        self.hp -= d

    def attack(self, actor):
        damage = self.damage()

        if constant.DEBUG == True:
            print '%s attack %s make %d damage.' % (self.name, actor.name, damage)

        actor.beAttacked(damage)
