import pygame as py
import json

import loader, factory



class Game:
    def __init__(self):
        self.screen = py.display.set_mode((800, 600))
        
        
    def load_extentions(self):
        with open("plugins.json", "r") as file:
            data = json.load(file)
            
            
            loader.load_modules(data["plugins"])
            
            self.character = [factory.create(character) for character in data["characters"]]
            
        
        
    def run(self):
        running = True
        while running:
            
            self.screen.fill((0, 0, 0))
            
            for character in self.character:
                character.update(self.screen)
            
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