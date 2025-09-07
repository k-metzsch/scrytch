import pygame

class Motion:
    def __init__(self, sprite):
        self.sprite = sprite
        self.rotate_degrees = 0
        
    def turn(self, degrees):
        self.rotate_degrees += degrees
        self.sprite.image_rotated = pygame.transform.rotate(self.sprite.image, self.rotate_degrees)
        self.sprite.position = self.sprite.image_rotated.get_rect(center=self.sprite.center)

    def go_to(self, x, y):
        self.sprite.position = [x, y]

    def glide(self, secs, x, y):
        # Optional: implement smooth movement over time if needed
        self.sprite.position = [x, y]

    def point_in_direction(self, degrees):
        self.sprite.image_rotated = pygame.transform.rotate(self.sprite.image, degrees)
        self.sprite.position = self.sprite.image_rotated.get_rect(center=self.sprite.center)
        pass

    def point_towards(self, target_sprite):
        # Optional: implement pointing logic if needed
        pass

    def change_x_by(self, amount):
        self.sprite.center.x += amount
        self.sprite.position = self.sprite.image_rotated.get_rect(center=self.sprite.center)

    def change_x_to(self, amount):
        self.sprite.position[0] = amount

    def change_y_by(self, amount):
        self.sprite.center.y += amount
        self.sprite.position = self.sprite.image_rotated.get_rect(center=self.sprite.center)

    def change_y_to(self, amount):
        self.sprite.position[1] = amount
