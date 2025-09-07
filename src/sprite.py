import pygame
from src.motion import Motion
from src.looks import Looks


class Sprite(Motion, Looks):
    def __init__(self, image_path, position=(0, 0), size=None, shown=True, direction=0):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.size = (size, size)
        self.image = self._get_scaled_image(self.original_image, size)
        self.center = pygame.math.Vector2(position)  # Store the intended center
        self.image_rotated = pygame.transform.rotate(self.image, direction)
        self.position = self.image_rotated.get_rect(center=self.center)
        self.shown = shown
        self.rotate_degrees = 0
        super().__init__(self)

    def _get_scaled_image(self, image, size):
        if size:
            return pygame.transform.smoothscale(image, (size, size))
        return image

    def set_size(self, size):
        self.size = (size, size)
        self.image = self._get_scaled_image(self.original_image, size)

    def show(self):
        self.shown = True

    def hide(self):
        self.shown = False

    def _draw(self, screen):
        if self.shown:
            screen.blit(self.image_rotated, self.position)
