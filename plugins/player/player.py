import pygame as py
from enum import Enum
from typing import Optional

import factory
from .player_movement_system import MovementSystem
from .borders_collisions import CollisionWithWallDetector
    


class Player(py.sprite.Sprite):
    def __init__(self, x : int, y : int, speed : int = 1):
        super().__init__()
        self.x = x
        self.y = y
        
        
        self.image = py.Surface((100, 100))
        self.image.fill((255, 0, 0))
        self.rect : py.rect.Rect = self.image.get_rect()
        self.movement_system = MovementSystem(speed)
        self.collison_with_wall_detector = CollisionWithWallDetector()
        self.i = 0
        
    
    def update(self, screen : py.surface.Surface, group : Optional[py.sprite.Group] = None): #type: ignore
        if group is None:
            raise ValueError("group is None")
        
        for sprite in group:
            if sprite is self:
                continue
            
            if sprite.rect is not None and self.rect.colliderect(sprite.rect):
                print("collision", self.i)
                self.i += 1
        
        self.movement_system.handle_input()
        self.rect = self.movement_system.move(self.rect)
        
        if self.collison_with_wall_detector.is_colliding_with_screen_borders(self.rect, screen):
            self.rect = self.collison_with_wall_detector.move_outside_screen_borders(self.rect, screen)
    
    def draw(self, screen : py.surface.Surface):
        py.draw.rect(screen, (255, 0, 0), self.rect)
        
        

        
        
        
def register() -> None:
    factory.register("player", Player)