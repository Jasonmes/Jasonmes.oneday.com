#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

import pygame

Screen_width = 309
Screen_legth = 500

def mian():
    pygame.init()
    window = pygame.display.set_mode((Screen_width, Screen_legth))
    img = pygame.image.load("/Users/jason/Downloads/发动机.jpg")
    pygame.display.set_caption('Hello World!')
    while True:
        window.blit(img, (0, 0))
        pygame.display.update()

mian()
