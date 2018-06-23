#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 异常处理
from moreM import *

try:
    path = input(":")
    with open(path, "r") as file:
        content = file.read()
        print(content)
except F:
    print("有问题哦")