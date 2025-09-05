class Motion:
    def __init__(self, sprite):
        self.sprite = sprite

    def turn(self, degrees):
        # Optional: implement rotation logic if you support it
        pass

    def go_to(self, x, y):
        self.sprite.position = [x, y]

    def glide(self, secs, x, y):
        # Optional: implement smooth movement over time if needed
        self.sprite.position = [x, y]

    def point_in_direction(self, degrees):
        # Optional: implement direction logic if needed
        pass

    def point_towards(self, target_sprite):
        # Optional: implement pointing logic if needed
        pass

    def change_x_by(self, amount):
        self.sprite.position[0] += amount

    def change_x_to(self, amount):
        self.sprite.position[0] = amount

    def change_y_by(self, amount):
        self.sprite.position[1] += amount

    def change_y_to(self, amount):
        self.sprite.position[1] = amount
