import pygame as py


class CollisionWithWallDetector:
    def is_colliding_with_screen_borders(self, rect : py.rect.Rect, screen : py.surface.Surface) -> bool:
        screen_width, screen_height = screen.get_size()
        
        colliding_top = rect.top < 0
        colliding_bottom = rect.bottom > screen_height
        colliding_left = rect.left < 0
        colliding_right = rect.right > screen_width
        
        return colliding_top or colliding_bottom or colliding_left or colliding_right
    
    def move_outside_screen_borders(self, rect : py.rect.Rect, screen : py.surface.Surface) -> py.rect.Rect:
        screen_width, screen_height = screen.get_size()
        
        if rect.top < 0:
            rect.top = 0
        elif rect.bottom > screen_height:
            rect.bottom = screen_height
            
        if rect.left < 0:
            rect.left = 0
        elif rect.right > screen_width:
            rect.right = screen_width
            
        return rect