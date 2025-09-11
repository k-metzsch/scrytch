import math
import threading
import time

import pygame


class Motion:
    def __init__(self, sprite):
        self.sprite = sprite
        self.window_width, self.window_height = pygame.display.get_surface().get_size()
        self.rotate_degrees = 0
        self._glide_thread = None
        self._glide_stop = threading.Event()
        self.__movement_blocked = False

    def __update_position(self):
        self.sprite.rect.center = self.sprite.center

    @property
    def mouse(self):
        return pygame.mouse

    def turn(self, degrees: int):
        if self.__movement_blocked:
            return

        self.rotate_degrees += degrees
        self.sprite.__set_rotation(self.rotate_degrees)
        self.__update_position()

    def go_to(self, x, y):
        if self.__movement_blocked:
            return

        self.sprite.center.x = x
        self.sprite.center.y = y
        self.__update_position()

    def __animate_glide(self, target, speed: int, fps: int, force: bool):
        # Force disable all other animation besides stop_glide
        if force:
            self.__movement_blocked = True

        while not self._glide_stop.is_set():
            direction = target - self.sprite.center
            distance = direction.length()

            if distance < speed or distance == 0:
                self.sprite.center = target
                self.__update_position()
                break

            # Snap into into target location
            direction = direction.normalize()
            self.sprite.center += direction * speed
            self.__update_position()
            time.sleep(1 / fps)

        if force:
            self.__movement_blocked = False

    def glide(self, speed: int, target_x: int, target_y: int, force: bool = True):
        self._glide_stop.set()

        if self._glide_thread and self._glide_thread.is_alive():
            self._glide_thread.join()

        self._glide_stop.clear()
        target = pygame.math.Vector2(target_x, target_y)
        self._glide_thread = threading.Thread(
            target=self.__animate_glide, args=(target, speed, 60, force)
        )
        self._glide_thread.daemon = True
        self._glide_thread.start()

    def glide_to_mouse(self, speed: int, force: bool = True):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.glide(speed, mouse_x, mouse_y, force)

    def stop_glide(self):
        self._glide_stop.set()
        if self._glide_thread and self._glide_thread.is_alive():
            self._glide_thread.join()

    def point_in_direction(self, degrees: int):
        if self.__movement_blocked:
            return

        self.sprite._set_rotation(degrees)
        self.__update_position()

    def point_towards(self, target):
        if self.__movement_blocked:
            return

        target_x, target_y = target.get_pos()
        dx = target_x - self.sprite.center.x
        dy = target_y - self.sprite.center.y
        self.rotate_degrees = math.degrees(math.atan2(-dy, dx))
        self.sprite._set_rotation(self.rotate_degrees)
        self.__update_position()

    def change_x_by(self, x: int):
        if self.__movement_blocked:
            return

        self.sprite.center.x += x
        self.__update_position()

    def change_x_to(self, x: int):
        if self.__movement_blocked:
            return

        self.sprite.center.x = x
        self.__update_position()

    def change_y_by(self, y: int):
        if self.__movement_blocked:
            return

        self.sprite.center.y += y
        self.__update_position()

    def change_y_to(self, y: int):
        if self.__movement_blocked:
            return

        self.sprite.center.y = y
        self.__update_position()

    def if_on_edge_bounce(self):
        rect = self.sprite.rect
        changed = False
        # Clamp left
        if rect.left < 0:
            rect.left = 0
            changed = True
        # Clamp right
        if rect.right > self.window_width:
            rect.right = self.window_width
            changed = True
        # Clamp top
        if rect.top < 0:
            rect.top = 0
            changed = True
        # Clamp bottom
        if rect.bottom > self.window_height:
            rect.bottom = self.window_height
            changed = True
        # If clamped, update center so future movements work correctly
        if changed:
            self.sprite.center = pygame.math.Vector2(rect.center)

