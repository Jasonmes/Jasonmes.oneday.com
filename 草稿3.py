#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess


# class dog(object):
#     def __init__(self):
#         self.__age = None
#
#     def set_age(self, age):
#         if age >= 0:
#             self.__age = age
#         else:
#             self.__info()
#
#     def set_get(self):
#         return self.__age
#
#     def __info(self):
#         print("wrong")
#
#
# giu = dog()
# giu.set_age(-10)
# print(giu.set_get())

class fish(object):
    def __init__(self):
        self.__name = "狗仔"

    def set_name(self, name):
        if name is not None:
            self.__name = name
            print(self.__name)
        else:
            self.__info()

    def __info(self):
        print("wrong")

    def get_name(self, name):
        return self.set_name(name)

    # def __del__(self):
    #     print("%s走了" % self.__name)

saa = fish()
ass = fish()
del saa
print(ass.get_name("宝贝宝贝"))