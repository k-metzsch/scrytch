import pygame
from src.motion import Motion


class Sprite(Motion):
    def __init__(self, image_path, position=(0, 0), size=None, shown=True):
        super().__init__(self)
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.size = (size, size)
        self.image = self._get_scaled_image(self.original_image, size)
        self.position = list(position)
        self.shown = shown

    def _get_scaled_image(self, image, size):
        if size:
            return pygame.transform.smoothscale(image, (size, size))
        return image

    def set_size(self, size):
        self.size = (size, size)
        self.image = self._get_scaled_image(self.original_image, self.size)

    def show(self):
        self.shown = True

    def hide(self):
        self.shown = False

    def draw(self, screen):
        if self.shown:
            screen.blit(self.image, self.position)
