import pygame
from src.motion import Motion
from src.looks import Looks

class Sprite(pygame.sprite.Sprite, Motion, Looks):
    def __init__(self, main, image_path, position=(0, 0), size=None, shown=True, direction=0):
        pygame.sprite.Sprite.__init__(self)
        Motion.__init__(self, self, main.window_size)
        Looks.__init__(self)

        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.size = size if size else self.original_image.get_size()
        self.image = self.__get_scaled_image(self.original_image, self.size)
        self.rotate_degrees = direction
        self.image = pygame.transform.rotate(self.image, self.rotate_degrees)

        self.rect = self.image.get_rect(center=position)
        self.center = pygame.math.Vector2(self.rect.center)
        self.shown = shown

    def get_pos(self):
        return self.center

    def get_rect(self):
        return self.rect

    def __get_scaled_image(self, image, size):
        if size:
            if isinstance(size, tuple):
                return pygame.transform.smoothscale(image, size)
            else:
                return pygame.transform.smoothscale(image, (size, size))
        return image

    def set_size(self, size):
        self.size = size
        self.image = self.__get_scaled_image(self.original_image, size)
        self.image = pygame.transform.rotate(self.image, self.rotate_degrees)
        self._update_rect()

    def set_rotation(self, degrees):
        self.rotate_degrees = degrees
        self.image = self.__get_scaled_image(self.original_image, self.size)
        self.image = pygame.transform.rotate(self.image, self.rotate_degrees)
        self._update_rect()

    def _update_rect(self):
        prev_center = self.center
        self.rect = self.image.get_rect(center=prev_center)
        self.center = pygame.math.Vector2(self.rect.center)

    def show(self):
        self.shown = True

    def hide(self):
        self.shown = False

    def _draw(self, screen):
        if self.shown:
            screen.blit(self.image, self.rect)