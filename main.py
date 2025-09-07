from engine import Engine
from scrython import Scrython
from src.sprite import Sprite


class Main(Scrython, Engine):
    def __init__(self, width=800, height=600, title="Scrython"):
        Scrython.__init__(self)
        Engine.__init__(self, self, width, height, title)

    def sprites(self):
        self.cat = Sprite(self, "sprites/cat.svg", position=(100, 100), size=(80, 80), shown=True)
        self.cat2 = Sprite(self, "sprites/cat.svg", position=(200, 200), size=(50, 50), shown=True)
        return [self.cat, self.cat2]

    def logic(self):
        self.when_key_is_pressed("d", self.move_right)
        self.when_key_is_pressed("a", self.move_left)
        self.when_key_is_pressed("s", self.move_down)
        self.when_key_is_pressed("w", self.move_up)
        self.when_key_is_pressed("space", self.point)

    def move_right(self):
        self.cat.change_x_by(10)
        self.cat.if_on_edge_bounce()
        
    def move_left(self):
        self.cat.change_x_by(-10)
        self.cat.if_on_edge_bounce()

    def move_down(self):
        self.cat.change_y_by(10)
        self.cat.if_on_edge_bounce()
    
    def move_up(self):
        self.cat.change_y_by(-10)
        self.cat.if_on_edge_bounce()
        
    def point(self):
        self.cat.glide(5, 400, 300, True)

if __name__ == "__main__":
    game_logic = Main()
    game_logic.run()