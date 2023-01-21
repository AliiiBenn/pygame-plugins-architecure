import pygame as py
from game import directions


class MovementSystem:
    def __init__(self, speed : int) -> None:
        
        self.direction = directions.Direction.NONE
        
        self.speed = speed
        
        
    def handle_input(self) -> None:
        keys = py.key.get_pressed()
        
        
        if keys[py.K_z]:
            self.direction = directions.Direction.UP
        elif keys[py.K_s]:
            self.direction = directions.Direction.DOWN
        elif keys[py.K_q]:
            self.direction = directions.Direction.LEFT
        elif keys[py.K_d]:
            self.direction = directions.Direction.RIGHT
        else:
            self.direction = directions.Direction.NONE
        
    
    def move(self, rect : py.rect.Rect) -> py.rect.Rect:
        return rect.move(self.direction.value * self.speed)