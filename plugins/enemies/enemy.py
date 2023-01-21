import pygame as py
import random
from typing import Optional

import factory

from .enemy_movement_system import MovementSystem


    

class Enemy(py.sprite.Sprite):
    def __init__(self, x : int, y : int, speed : int) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
        
        self.image = py.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect : py.rect.Rect = self.image.get_rect()
        
        self.movement_system = MovementSystem(self.speed)
        
        
    def update(self, screen : py.surface.Surface, group : Optional[py.sprite.Group] = None) -> None: #type: ignore
        
        self.movement_system.change_direction_randomly()
        self.rect = self.movement_system.move(self.rect)
    
    
    def draw(self, screen : py.surface.Surface) -> None:
        py.draw.rect(screen, (0, 255, 0), self.rect)
        
        
def register() -> None:
    factory.register("enemy", Enemy)