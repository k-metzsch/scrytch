import pygame
from src.keys import KEYS


class Events:
    def __init__(self):
        self.once = False
        self._started_handlers = []

    def when_started(self, handler):
        self._started_handlers.append(handler)

    def _run_started(self):
        if not self.once:
            for handler in self._started_handlers:
                handler()
            self.once = True

    def when_key_is_pressed(self, key: str, handler):
        keys = pygame.key.get_pressed()
        if keys[KEYS[key]]:
            handler()
