import asyncio
from abc import ABC, abstractmethod

import pygame

from Scrytch.events import Events
from Scrytch.looks import Looks
from Scrytch.motion import Motion
from Scrytch.sound import Sound


class Sprite(ABC, pygame.sprite.Sprite, Motion, Looks, Events, Sound):
    def __init__(
        self,
        image_path: str,
        position: tuple[int, int] = (0, 0),
        size: int | None = None,
        shown: bool = True,
        direction: int = 0,
    ):
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.size = size if size else self.original_image.get_size()
        self.image = self.get_scaled_image(self.original_image, self.size)
        self.rotate_degrees = direction
        self.image = pygame.transform.rotate(self.image, self.rotate_degrees)
        self.rect = self.image.get_rect(center=position)
        self.center = pygame.math.Vector2(self.rect.center)
        self.shown = shown

        pygame.sprite.Sprite.__init__(self)
        Motion.__init__(self, self)
        Looks.__init__(self, self)
        Events.__init__(self, self)
        Sound.__init__(self, self)

    @abstractmethod
    def events(self):
        pass

    def get_pos(self) -> pygame.math.Vector2:
        return self.center

    async def wait(self, seconds):
        await asyncio.sleep(seconds)

    def _switch_costume(self, costume_path: str):
        self.original_image = pygame.image.load(costume_path).convert_alpha()
        self.image = self.get_scaled_image(self.original_image, self.size)
        self.image = pygame.transform.rotate(self.image, self.rotate_degrees)
        self._update_rect()

    def get_scaled_image(
        self, image, size: int | tuple[int, int] | None
    ) -> pygame.Surface:
        if size:
            if isinstance(size, tuple):
                return pygame.transform.smoothscale(image, size)
            else:
                return pygame.transform.smoothscale(image, (size, size))
        return image

    def _set_rotation(self, degrees: int):
        self.rotate_degrees = degrees
        self.image = self.get_scaled_image(self.original_image, self.size)
        self.image = pygame.transform.rotate(self.image, self.rotate_degrees)
        self._update_rect()

    def _update_rect(self):
        prev_center = self.center
        self.rect = self.image.get_rect(center=prev_center)
        self.center = pygame.math.Vector2(self.rect.center)

    def _draw(self, screen: pygame.Surface):
        if self.shown:
            screen.blit(self.image, self.rect)

