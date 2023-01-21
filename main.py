import pygame as py
import json

import loader, factory



class Game:
    def __init__(self):
        self.screen = py.display.set_mode((800, 600))
        self.clock = py.time.Clock()
        self.entities = py.sprite.Group()
        
    def load_extentions(self):
        with open("plugins.json", "r") as file:
            data = json.load(file)
            
            
            loader.load_modules(data["plugins"])
            
            self.character = [factory.create(character) for character in data["characters"]]
            for character in self.character:
                self.entities.add(character) #type: ignore
            
        
        
    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            
            self.screen.fill((0, 0, 0))
            
            
            for entity in self.entities:
                entity.update(self.screen, self.entities)
                entity.draw(self.screen) #type: ignore
            
            py.display.update()
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                    
        py.quit()
        
        
    
if __name__ == "__main__":
    py.init()
    game = Game()
    game.load_extentions()
    game.run()