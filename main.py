from engine import Engine
from scrython import Scrython
from src.sprite import Sprite


class Main(Scrython, Engine):
    def sprites(self):
        self.cat = Sprite("sprites/cat.png", position=(100, 100), size=(80), shown=True)
        self.cat2 = Sprite("sprites/cat.png", position=(200, 200), size=(50), shown=True)
        return [self.cat, self.cat2]

    def logic(self, engine):
        self.when_key_is_pressed("d", self.move_right)
        self.when_key_is_pressed("a", self.move_left)
        self.when_key_is_pressed("s", self.move_down)
        self.when_key_is_pressed("w", self.move_up)
        self.when_key_is_pressed("space", self.point)

    def move_right(self):
        self.cat.change_x_by(5)
        self.cat.turn(5)
        
    def move_left(self):
        self.cat.stop_glide()
        self.cat.change_x_by(-5)
        self.cat.turn(-5)
        # self.cat.turn(-10)

    def move_down(self):
        self.cat.change_y_by(10)
    
    def move_up(self):
        self.cat.change_y_by(-10)
        
    def point(self):
        self.cat.glide(5, 400, 300)
        
if __name__ == "__main__":
    game_logic = Main()
    engine = Engine(game_logic)
    engine.run()
