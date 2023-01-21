from typing import Protocol, Optional
import pygame as py





class Character(Protocol):
    
    def update(self, screen : py.surface.Surface, group : Optional[py.sprite.Group] = None):
        ...
        
    def draw(self, screen : py.surface.Surface):
        ...