from game import directions
import pygame as py
import random



class MovementSystem:
    def __init__(self, speed : int) -> None:
        self.speed = speed
        self.direction = directions.Direction.NONE
        
        self.start_time = py.time.get_ticks()
        
    def change_direction_randomly(self) -> None:
        seconds = (py.time.get_ticks() - self.start_time) / 1000
        
        if seconds > 1:
            self.start_time = py.time.get_ticks()
            self.direction = random.choice(list(directions.Direction))
            
            
    def move(self, rect : py.rect.Rect) -> py.rect.Rect:
        return rect.move(self.direction.value * self.speed)