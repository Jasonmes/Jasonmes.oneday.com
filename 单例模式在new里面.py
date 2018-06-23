#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 单例写在new里面
# class Instance(object):
#     __instance = None
#     __hasinit = False
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             # 不能直接用类来调用否则就是个递归，死环，最好用object˜
#             cls.__instance = object.__new__(Instance)
#
#         return cls.__instance
#
#     def __init__(self):
#         if Instance.__hasinit is False:
#             Instance.__hasinit = True


class danli(object):
    # 保存初始地址，不被改变
    __dan = None
    def __new__(cls, *args, **kwargs):
        if cls.__dan is None:
            cls.__dan = object.__new__(danli)
        return cls.__dan

One = danli()
One._danli__dan = "花湖"

Two = danli()

print(id(One))
print(id(Two))


