from src.engine import Engine
from cat1 import Cat1
from cat2 import Cat2


class Main(Engine):
    def __init__(self, width=800, height=600, title="Scrython"):
        self.cat = None
        Engine.__init__(self, self, width, height, title)
        
    def sprites(self):
        self.cat1 = Cat1(self)
        self.cat2 = Cat2(self)
        return [self.cat1, self.cat2]


if __name__ == "__main__":
    Main().run()