#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

__all__ = ["func", "count"]

def func():
    pass

count = 0

# class Dog:
#     pass


class God(object):
    def __init__(self):
        self.name = "上帝哦"


class Dod(object):
    def __init__(self):
        self.name = "多的"

class cat(object):
    def eat(self, man):
        print("%s看到你了" % man.name)

Cat = cat()
god = God()
dod = Dod()
Cat.eat(dod)
