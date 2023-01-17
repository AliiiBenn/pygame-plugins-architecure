from typing import Protocol
import pygame as py


class Character(Protocol):
    
    def update(self, screen : py.surface.Surface):
        ...
        
    def draw(self, screen : py.surface.Surface):
        ...