import pygame


class Looks:
    def __init__(self, sprite):
        self.sprite = sprite
        
    def say(self, message, seconds):
        pass
    
    def think(self, message, seconds):
        pass
    
    def switch_costume(self, costume):
        pass

    def switch_backdrop(self, costume):
        pass
    
    def change_size(self, amount):
        pass
    
    def set_size_to(self, percent):
        pass
    
    def show(self):
        self.sprite.shown = True

    def hide(self):
        self.sprite.shown = False
        
    def go_to_layer(self, layer):
        pass