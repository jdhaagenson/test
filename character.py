"""
Setup all characters
"""
import pygame as pg


class CreatureStateMachine:
    def __init__(self):
        self.state = ""


class BaseCharacter(pg.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = self.rect.x, self.rect.y
        self.state = CreatureStateMachine()