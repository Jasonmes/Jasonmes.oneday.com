#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 练习题2
# 烤地瓜应用智能版
# 要求:
# 完善烤地瓜应用
# 先实现以下方法：
# cook() : 把地瓜烤一段时间
# addCondiments() : 给地瓜添加配料
# __init__() : 设置默认的属性
# __str__() : 让print的结果看起来更好一些
# 然后实现以下方法：
# auto_addCondiments(): 自动随机添加一种配料
# auto_cook(): 自动烤地瓜，当地瓜烤熟了，自动停止
# 提示：
# auto_cook方法使用循环，调用cook方法，每次循环都判断一次地瓜的状态，一旦地瓜烤熟了，就立刻使用break终止循环
# auto_addCondiments方法: 可以先在__init__方法中，为地瓜设计一个condiments属性，类型为列表，数据如["番茄酱","沙拉酱","芥末酱","辣椒酱"]等等，然后在调用cook方法时，随机选择一种，作为配料来添加
import random

class sweet_patato(object):
    def __init__(self):
        self.time = 0
        self.state = "生的"
        self.condiments = []

    def auto_cook(self, condiment):
        while True:
            self.time += 1
            if self.time <= 3:
                self.state = "半生未熟"
            elif 3 < self.time <= 6:
                self.state = "一般熟"
            elif 10 > self.time > 6:
                self.state = "熟了"
            else:
                self.state = "糊了"
            if self.time >= 9:
                self.condiments.append(condiment)
                break

    def auto_addCondiments(self):
        condiments = ["芥末", "椒盐", "盐巴", "白糖", "红糖"]
        return condiments[random.randint(0, 4)]

    def __str__(self):
        return "地瓜的状态%s,烤了%s分钟,佐料有%s" % (self.state, self.time, self.condiments)

Digua = sweet_patato()
Digua.auto_cook(Digua.auto_addCondiments())
print(Digua)


