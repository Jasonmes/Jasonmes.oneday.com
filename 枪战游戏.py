#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

class Man(object):
    __instance = None
    __hasinit = False
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(Man)
        return cls.__instance

    def __init__(self):
        if self.__hasinit is False:
            self.__hasinit = True
        self.name = None
        self.Life_value = 1000
        self.Bullet_num = 0
        self.GUN = None

    # def body_value(self):
    #     Body_Value = {"头": 1000,
    #                   "手": 800,
    #                   "脚": 600,
    #                   "胸腔": 700}

    # 枪的伤害值
    # 打中的位置的不同伤害值不同
    def damage(self, man, gun):
        guns = {"ak47": 28,
                "m416": 19,
                "kar98k": 600}
        # 中枪后生命值的减少
        for item in guns:
            if gun == item:
                man.Life_value -= guns[item]
                man.Bullet_num += 1
                man.GUN = gun
                if man.Life_value <= 0:
                    man.Life_value = 0
                    break
                return self.__str__()

    def shoot(self, man, gun):
        self.damage(man, gun)


    def __str__(self):
        return "账号%s, 生命值为%s, 中弹数量%s, 被%s射中" % (self.name, self.Life_value, self.Bullet_num, self.GUN)



