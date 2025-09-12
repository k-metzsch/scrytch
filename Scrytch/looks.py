import time
import pygame


class Looks:
    def __init__(self, sprite):
        self.sprite = sprite
        self._bubble_message = None
        
    def __set_size(self, size):
        self.sprite.size = size
        self.sprite.image = self.sprite.get_scaled_image(self.sprite.original_image, self.sprite.size)
        self.sprite._update_rect()
        
    def bubble(self, message, seconds=2, back_color=(255, 255, 255), text_color=(0, 0, 0)):
        self._bubble_message = (message, back_color, text_color)
        self._bubble_until = time.time() + seconds
        
    def _draw_bubble(self, screen):
        # Check if there's a message to display and if the time hasn't expired
        if self._bubble_message and time.time() < self._bubble_until:
            message, color, text_color = self._bubble_message
            font = pygame.font.SysFont(None, 24) # Default font and size
            text_surface = font.render(message, True, text_color)
            
            padding = 10
            bubble_width = text_surface.get_width() + padding * 2
            bubble_height = text_surface.get_height() + padding * 2

            # Set the position of the bubble above the sprite
            sprite_rect = self.sprite.rect
            bubble_x = sprite_rect.centerx - bubble_width / 2
            bubble_y = sprite_rect.top - bubble_height - 10

            # Draw the bubble
            bubble_rect = pygame.Rect(bubble_x, bubble_y, bubble_width, bubble_height)
            pygame.draw.rect(screen, color, bubble_rect, border_radius=15) # Rounded corners
            screen.blit(text_surface, (bubble_x + padding, bubble_y + padding))
    
    def switch_costume(self, costume_name):
        costume_dict = self.sprite.main._costumes
        if costume_name in costume_dict:
            self.sprite._switch_costume(costume_dict[costume_name])

    def switch_backdrop(self, backdrop_name):
        backdrop_dict = self.sprite.main._backdrops
        if backdrop_name in backdrop_dict:
            backdrop_path = backdrop_dict[backdrop_name]
            self.sprite.main._set_backdrop(backdrop_name, backdrop_path)  # Pass both path and name

    def change_size(self, amount):
        self.__set_size(self.sprite.size + amount)

    def set_size_to(self, amount): 
        self.__set_size(amount)
    
    def show(self):
        self.sprite.shown = True

    def hide(self):
        self.sprite.shown = False