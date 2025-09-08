from abc import ABC, abstractmethod
import pygame
from src.motion import Motion
from src.looks import Looks
from src.sensing import Sensing
from src.events import Events
from src.sound import Sound


class Sprite(ABC, pygame.sprite.Sprite, Motion, Looks, Sensing, Events, Sound):
    def __init__(self, image_path, position=(0, 0), size=None, shown=True, direction=0):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.size = size if size else self.original_image.get_size()
        self.image = self.__get_scaled_image(self.original_image, self.size)
        self.rotate_degrees = direction
        self.image = pygame.transform.rotate(self.image, self.rotate_degrees)
        self.rect = self.image.get_rect(center=position)
        self.center = pygame.math.Vector2(self.rect.center)
        self.shown = shown
        
        pygame.sprite.Sprite.__init__(self)
        Motion.__init__(self, self)
        Sensing.__init__(self, self)
        Looks.__init__(self, self)
        Events.__init__(self, self)
        Sound.__init__(self, self)
        
    @abstractmethod
    def logic(self):
        pass

    def __get_scaled_image(self, image, size):
        if size:
            if isinstance(size, tuple):
                return pygame.transform.smoothscale(image, size)
            else:
                return pygame.transform.smoothscale(image, (size, size))
        return image

    def _set_rotation(self, degrees):
        self.rotate_degrees = degrees
        self.image = self.__get_scaled_image(self.original_image, self.size)
        self.image = pygame.transform.rotate(self.image, self.rotate_degrees)
        self._update_rect()

    def _update_rect(self):
        prev_center = self.center
        self.rect = self.image.get_rect(center=prev_center)
        self.center = pygame.math.Vector2(self.rect.center)

    def _draw(self, screen):
        if self.shown:
            screen.blit(self.image, self.rect)