#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# class giteng(object):
#     pass
#
# def geteng_():
#     new_obj = giteng.__new__(giteng)
#     new_obj.__init__()
#     return new_obj
#
# hub = geteng_()
# print(hub)


class GIO(object):
    # def __new__(cls, *args, **kwargs):
    #     print("调用new方法")

    def __init__(self):
        self.color = "ahahah"
        print("调用了初始化")

    def pos(self):
        print("我还没有被改写")


# def god():
#     new_obj = GIO.__new__(GIO)
#     return new_obj

class gio(GIO):
    def pos(self):
        # super调用类方法
        super(gio, self).pos()
        super().pos()
        print("被改写了")

    # def __new__(cls, *args, **kwargs):
    #     super().__new__(cls, *args, **kwargs)
    #     print("改写了new方法")


    def __init__(self):
        super().__init__()
        self.color = "aasdad"

test = gio()
# test.pos()
print(test.color)

