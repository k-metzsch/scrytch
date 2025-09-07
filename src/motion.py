import threading
import time
import pygame
import math

class Motion:
    def __init__(self, sprite, window_size):
        self.sprite = sprite
        self.window_width, self.window_height = window_size
        self.rotate_degrees = 0
        self._glide_thread = None
        self._glide_stop = threading.Event()
        self._movement_blocked = False

    def __update_position(self):
        self.sprite.rect.center = self.sprite.center

    def turn(self, degrees):
        if self._movement_blocked:
            return
        self.rotate_degrees += degrees
        self.sprite.set_rotation(self.rotate_degrees)
        self.__update_position()

    def go_to(self, x, y):
        if self._movement_blocked:
            return
        self.sprite.center.x = x
        self.sprite.center.y = y
        self.__update_position()

    def __animate_glide(self, target, speed, fps, force):
        # Force disable all other animation besides stop_glide
        if force:
            self._movement_blocked = True
        while not self._glide_stop.is_set():
            direction = target - self.sprite.center
            distance = direction.length()
            if distance < speed or distance == 0:
                self.sprite.center = target
                self.__update_position()
                break
            direction = direction.normalize()
            self.sprite.center += direction * speed
            self.__update_position()
            time.sleep(1 / fps)
        if force:
            self._movement_blocked = False

    def glide(self, speed, target_x, target_y, force=False, fps=60):
        self._glide_stop.set()
        if self._glide_thread and self._glide_thread.is_alive():
            self._glide_thread.join()
        self._glide_stop.clear()
        target = pygame.math.Vector2(target_x, target_y)
        self._glide_thread = threading.Thread(target=self.__animate_glide, args=(target, speed, fps, force))
        self._glide_thread.daemon = True
        self._glide_thread.start()
    
    def stop_glide(self):
        self._glide_stop.set()
        if self._glide_thread and self._glide_thread.is_alive():
            self._glide_thread.join()

    def point_in_direction(self, degrees):
        if self._movement_blocked:
            return
        self.sprite.set_rotation(degrees)
        self.__update_position()

    def point_towards(self, target):
        if self._movement_blocked:
            return
        target_x, target_y = target.get_pos()
        dx = target_x - self.sprite.center.x
        dy = target_y - self.sprite.center.y
        self.rotate_degrees = math.degrees(math.atan2(-dy, dx))
        self.sprite.set_rotation(self.rotate_degrees)
        self.__update_position()

    def change_x_by(self, x):
        if self._movement_blocked:
            return
        self.sprite.center.x += x
        self.__update_position()

    def change_x_to(self, x):
        if self._movement_blocked:
            return
        self.sprite.center.x = x
        self.__update_position()

    def change_y_by(self, y):
        if self._movement_blocked:
            return
        self.sprite.center.y += y
        self.__update_position()

    def change_y_to(self, y):
        if self._movement_blocked:
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