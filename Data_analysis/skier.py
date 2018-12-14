# -*- coding: utf-8 -*-
"""
@author: Yangdan
"""
import pygame
import random
import sys

skier_images=['skier_down.png','skier_left1.png','skier_left2.png','skier_right1.png',
              'skier_right2.png','skier_tree.png','skier_flag.png']

# 创建滑雪者
class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('skier_down.png')
        self.rect=self.image.get_rect()
        self.rect.center=[320,100]
        self.angle=0

