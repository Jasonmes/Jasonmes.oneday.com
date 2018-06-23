#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

class Shopping_cart(object):
    # 记录创造出来的对象
    __instance = None
    def __new__(cls, *args, **kwargs):
        # 重写创建对象的方法
        # 调用父类的new方法创建对象
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        # 如果创建直接返回创建过的对象
        return cls.__instance

cart1 = Shopping_cart()
print(cart1)
