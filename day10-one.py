#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 练习题1
#
# 编写一段代码以完成下面的要求
#
# 要求：
#
# 定义一个人的基类,类中要有初始化方法,方法中要有人的姓名,年龄.
# 将类中的姓名和年龄私有化.
# 提供获取用户信息的函数.
# 提供获取私有属性的方法.
# 提供可以设置私有属性的函数.
# 设置年龄的范围(0-100).
# 提示：
#
# 将公有属性变为私有属性的方法是在其前面加上__即可.
class Invisible(object):
    def __init__(self):
        self.__name = "花花"
        self.__age = 19

    def get_info(self):
        return self.__name, self.__age

def user_info(name, age):
    print(name, age)

def age(age):
    if 0 < age < 100:
        print("已经设置˜")

vis = Invisible()

print(vis._Invisible__age)

# for i in dir(vis):
#     print(i)

# ---->_Invisible__age
# ---->_Invisible__name

