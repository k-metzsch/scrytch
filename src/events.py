import pygame
import threading
from src.keys import KEYS


class Events:
    def __init__(self, sprite):
        self.sprite = sprite
        self.once = False
        self._old_backdrop = None

    def when_started(self, handler):
        if not self.once:
            threading.Thread(target=handler).start()
            self.once = True

    def when_key_is_pressed(self, key: str, handler):
        keys = pygame.key.get_pressed()
        if keys[KEYS[key]]:
            threading.Thread(target=handler).start()
            
    def when_sprite_clicked(self, handler):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        if self.sprite.rect.collidepoint(mouse_pos) and mouse_buttons[0]:
            threading.Thread(target=handler).start()

    def when_backdrop_switches_to(self, backdrop_name=None, handler=None):
        if backdrop_name is None:
            backdrop_dict = self.sprite.main.backdrops()
            if backdrop_dict:
                backdrop_name = next(iter(backdrop_dict.keys()))
            else:
                return
                
        # Get the current backdrop name from the tuple
        current_backdrop_name = None
        if self.sprite.main.background_image:
            current_backdrop_name = self.sprite.main.background_image[0]

        if current_backdrop_name == backdrop_name and self._old_backdrop != current_backdrop_name:
            if handler:
                threading.Thread(target=handler).start()
        self._old_backdrop = current_backdrop_name

    def when_i_receive_message(self, message, handler):
        broadcast_bus.register(message, handler)

    def broadcast_message(self, message):
        broadcast_bus.broadcast(message)
        
    def broadcast_message_and_wait(self, message):
        broadcast_bus.broadcast_and_wait(message)
    

class BroadcastBus:
    def __init__(self):
        self.listeners = {}

    def register(self, message, handler):
        self.listeners.setdefault(message, []).append(handler)

    def broadcast(self, message):
        for handler in self.listeners.get(message, []):
            threading.Thread(target=handler).start()
            
    def broadcast_and_wait(self, message):
        threads = []
        for handler in self.listeners.get(message, []):
            t = threading.Thread(target=handler)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

broadcast_bus = BroadcastBus()