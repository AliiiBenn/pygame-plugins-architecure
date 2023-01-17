import pygame as py
from dataclasses import dataclass

import factory


class Player:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        print('player created')
    
    def update(self, screen : py.surface.Surface):
        self.draw(screen)
        self.move()
    
    def draw(self, screen : py.surface.Surface):
        py.draw.rect(screen, (255, 0, 0), (self.x, self.y, 100, 100))
        
        
    def move(self):
        pass
        
        
        
def register() -> None:
    factory.register("player", Player)