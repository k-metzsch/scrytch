import asyncio
import pygame
from src.keys import KEYS

class Events:
    def __init__(self, sprite):
        self.sprite = sprite
        self.once = False
        self._old_backdrop = None
        self._keys_down = set()
        self._sprite_click_down = False

    def _schedule(self, handler):
        """Schedule handler: if async -> task, else offload to thread."""
        if asyncio.iscoroutinefunction(handler):
            asyncio.create_task(handler())
        else:
            asyncio.create_task(asyncio.to_thread(handler))

    def when_started(self, handler):
        if not self.once:
            self._schedule(handler)
            self.once = True

    def when_key_is_pressed(self, key: str, handler):
        """Continuously invoke handler every frame while key is held (no threads)."""
        keys = pygame.key.get_pressed()
        if keys[KEYS[key]]:
            # Inline call for lightweight handlers; schedule if coroutine
            if asyncio.iscoroutinefunction(handler):
                asyncio.create_task(handler())
            else:
                handler()

    def when_sprite_clicked(self, handler):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        over = self.sprite.rect.collidepoint(mouse_pos)
        pressed = mouse_buttons[0]
        if over and pressed and not self._sprite_click_down:
            self._sprite_click_down = True
            self._schedule(handler)
        elif not pressed:
            self._sprite_click_down = False

    def when_backdrop_switches_to(self, backdrop_name=None, handler=None):
        if backdrop_name is None:
            backdrop_dict = self.sprite.main.backdrops()
            if backdrop_dict:
                backdrop_name = next(iter(backdrop_dict.keys()))
            else:
                return

        current_backdrop_name = None
        if self.sprite.main.background_image:
            current_backdrop_name = self.sprite.main.background_image[0]

        if current_backdrop_name == backdrop_name and self._old_backdrop != current_backdrop_name:
            self._schedule(handler)
        self._old_backdrop = current_backdrop_name

    def when_i_receive_message(self, message, handler):
        broadcast_bus.register(message, handler)

    def broadcast_message(self, message):
        # Fire-and-forget; schedule async broadcast without blocking the frame
        asyncio.create_task(broadcast_bus.broadcast(message))

    async def broadcast_message_and_wait(self, message):
        await broadcast_bus.broadcast_and_wait(message)


class BroadcastBus:
    # A simple system for broadcasting messages between sprites
    def __init__(self):
        self.listeners = {}

    def register(self, message, handler):
        self.listeners.setdefault(message, []).append(handler)

    async def broadcast(self, message):
        for handler in self.listeners.get(message, []):
            if asyncio.iscoroutinefunction(handler):
                asyncio.create_task(handler())
            else:
                asyncio.create_task(asyncio.to_thread(handler))

    # Broadcast a message and wait for listeners registered at the time of call
    async def broadcast_and_wait(self, message):
        tasks = []
        for handler in list(self.listeners.get(message, [])):
            if asyncio.iscoroutinefunction(handler):
                tasks.append(asyncio.create_task(handler()))
            else:
                tasks.append(asyncio.create_task(asyncio.to_thread(handler)))
        if tasks:
            await asyncio.gather(*tasks)

broadcast_bus = BroadcastBus()