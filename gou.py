#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess


# python读取文件实现嵌套列表
# def read_date(file_name):
#     if not re.findall(".txt", file_name):
#         file_name += ".txt"
# L = [[] for h in [[] for k in range(5)]]
#     # with open(file_name) as r:
#     #     for d in r:
#     #         j = d.split("|")
# # for i in range(len(L)):
# #     L[i].append()
# # return L
# print(L)
# m = [[] for j in range(5)]
# print(m)


# sew = (1, 1, 2, 2, 3, 4, 4)
# for item in sew:
#     print(item)
# s = set(sew)
#
# print(set(s))

class DOg(object):
    def eat(self):
        print("小狗来了")
    pass

def dog_new():
    dog = DOg.__new__(DOg)
    dog.__init__()
    return dog

do = dog_new()
do1 = DOg()
do1.eat()
do.eat()
