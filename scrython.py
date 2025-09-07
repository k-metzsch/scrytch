from abc import ABC, abstractmethod
from src.events import Events
from src.looks import Looks
from src.sensing import Sensing
from src.sound import Sound
import pygame


class Scrython(ABC, Events, Looks, Sensing, Sound):
    def __init__(self):
        Events.__init__(self)
        Looks.__init__(self)
        Sensing.__init__(self)
        Sound.__init__(self)
        
    def mouse(self):
        return pygame.mouse
    
    @abstractmethod
    def sprites(self):
        return []

    @abstractmethod
    def logic(self):
        pass
