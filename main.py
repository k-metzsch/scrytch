from src.engine import Engine
from testsprite import TestSprite


class Main(Engine):
    def __init__(self, width=800, height=600, title="Scrython"):
        Engine.__init__(self, self, width, height, title)

    def sprites(self):
        return [TestSprite()]
        

if __name__ == "__main__":
    Main().run()