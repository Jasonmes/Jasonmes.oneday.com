#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

# 一开始我以为不需要设置枪的类，后来我明白，其实还是需要的，玩家捡到枪，还是需要传入一个枪的实例对象
# 不急，慢慢写

# 枪战游戏
# 需要把单例写进去吗？
class GUN(object):
    # __instance = None
    # __hasinit = False
    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = object.__new__(GUN)
    #     return cls.__instance

    def __init__(self):
        # if GUN.__hasinit is False:
        #     GUN.__hasinit = True
        self.name = None
        # 这里是统一所有的枪都是20发子弹
        # 好吧，按照自己的想法来写
        self.bullet = 20
        # 弹夹
        self.danjia = 2
        # 没关系的，这些都是可以被重写的
        self.damage = 20


    def add_bullet(self, count):
        if count < 0:
            return
        else:
            print("》》》》%s已经添加%s颗子弹" % (self.name, count))
        self.bullet += count
        if self.bullet == 0:
            self.danjia = 3
            print("子弹不足，请添加子弹,弹夹数量%s" % self.danjia)
        elif self.bullet <= 20:
            print("弹夹还剩下%s,子弹数量%s" % (self.danjia, self.bullet))
        elif 20 < self.bullet <= 40:
            self.danjia = 1
            print("弹夹还剩下%s,子弹数量%s" % (self.danjia, self.bullet))
        elif 40 < self.bullet <= 60:
            self.danjia = 0
            print("弹夹还剩下%s,子弹数量%s" % (self.danjia, self.bullet))

    def shoot(self, enemy):
        """

        :type enemy: Player
        """
        if self.bullet > 0:
            print("  %s被射中" % enemy.name)
        else:
            print("子弹不足")
            return
        self.bullet -= 1
        if self.bullet == 0:
            self.danjia = 3
            self.bullet = 0
            print("子弹不足，请添加子弹,弹夹数量%s个" % self.danjia)
        elif self.bullet <= 20:
            print("  弹夹还剩下%s个,子弹数量%s" % (self.danjia, self.bullet))
        elif 20 < self.bullet <= 40:
            self.danjia = 1
            print("  弹夹还剩下%s个,子弹数量%s" % (self.danjia, self.bullet))
        elif 40 < self.bullet <= 60:
            self.danjia = 0
            print("  弹夹还剩下%s个,子弹数量%s" % (self.danjia, self.bullet))

        # 这里忽略enemy被打中的几率，只要shoot，enemy就受伤，生命值减少，警察子弹减少弹夹也少
        enemy.life_value -= self.damage
        # enemy.shoot_by_Gun.append[self.name]
        enemy.shoot_bulletCount += 1
        if enemy.life_value <= 0:
            enemy.life_value = 0
            enemy.state = "再接再厉"
            print("  %s被淘汰了" % enemy.name)
        print(enemy)
        # 等一下再添加


class Player(object):
    def __init__(self):
        self.life_value = 1000
        self.name = None
        self.GUN_have = None
        self.shoot_bulletCount = 0
        # 添加枪的对象
        # self.shoot_by_Gun = []
        self.state = "活的"

    # 这里是重点
    def fire(self, gun, enemy):
        self.GUN_have = gun
        if self.GUN_have is not None:
            print("%s捡到了%s" % (self.name, self.GUN_have.name))
        self.GUN_have.shoot(enemy)



    # 吃药
    # 移动
    # 礽东西
    # 给其他玩家发信息

    def __str__(self):
        if self.life_value <= 0:
            return '  %s的生命值还剩下%s，中弹量%s，状态被淘汰了' % (self.name, self.life_value, self.shoot_bulletCount)
        else:
            return '  %s的生命值还剩下%s，中弹量%s，状态%s' % (self.name, self.life_value, self.shoot_bulletCount, self.state)



ak47 = GUN()
ak47.name = "ak47"
ak47.damage = 50

kar98k = GUN()
kar98k.name = "kar98k"
kar98k.bullet = 1
kar98k.damage = 600

houhou = Player()
xiaoming = Player()
houhou.name = "盗贼"
xiaoming.name = "小明"
kar98k.add_bullet(200)
i = 1
while True:
    print("===============第%s轮对决===============" % i)
    xiaoming.fire(ak47, houhou)
    # houhou.fire()
    if ak47.bullet < 0 or houhou.life_value <= 0 or ak47.bullet <= 0:
        break
    i += 1

