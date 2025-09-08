import pygame
from src.keys import KEYS


class Events:
    def __init__(self, sprite):
        self.sprite = sprite
        self.once = False

    def when_started(self, handler):
        if not self.once:
            handler()
            self.once = True

    def when_key_is_pressed(self, key: str, handler):
        keys = pygame.key.get_pressed()
        if keys[KEYS[key]]:
            handler()
            
    def when_sprite_clicked(self, handler):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        if self.sprite.rect.collidepoint(mouse_pos) and mouse_buttons[0]:
            handler()

    def when_backdrop_switches_to(self, backdrop, handler):
        pass
    
    def when_i_receive_message(self, message, handler):
        pass
    
    def broadcast_message(self, message):
        pass