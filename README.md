# Scrytch

**Scrytch** is a Python project that imitates Scratch game logic, making it easier to create interactive games and animations using Python. Built on top of [pygame](https://www.pygame.org/), Scrytch provides a simple API for sprites, backdrops, sounds, and more—ideal for educational projects, prototypes, or anyone who loves Scratch’s workflow but wants to use Python.

---

## Installation

You can install Scrytch from PyPI:

```bash
pip install Scrytch
```

Or install from source:

```bash
git clone https://github.com/k-metzsch/scrytch.git
cd scrytch
pip install .
```

---

## Basic Usage Example

Below is a minimal example showing how to set up a sprite and the main game class.

### (Sprite Example)

```python
from Scrytch.sprite import Sprite

class Cat(Sprite):
    def __init__(self, main):
        Sprite.__init__(
            self,
            image_path="sprites/cat.svg",
            position=(50, 80),
            size=(100),
            shown=True,
        )
        self.main = main

    def events(self):
        self.when_key_is_pressed("w", self.move_up)
        self.when_key_is_pressed("s", self.move_down)
        self.when_key_is_pressed("a", self.move_left)
        self.when_key_is_pressed("d", self.move_right)

    async def move_up(self):
        self.change_y_by(-10)

    async def move_down(self):
        self.change_y_by(10)

    async def move_right(self):
        self.change_x_by(10)

    def move_left(self):
        self.change_x_by(-10)
```

---

### (Main Game Example)

```python
import asyncio

from cat1 import Cat1
from cat2 import Cat2
from Scrytch.scrytch import Scrytch

class Main(Scrytch):
    def __init__(self, width=800, height=600, title="Scrython"):
        Scrytch.__init__(self, self, width, height, title)

    def sprites(self):
        self.cat1 = Cat1(self)
        self.cat2 = Cat2(self)
        return [self.cat1, self.cat2]

    def backdrops(self):
        self._backdrops = {
            "backdrop1": "backdrops/backdrop1.jpg",
            "backdrop2": "backdrops/backdrop2.jpg",
        }
        return self._backdrops

    def sounds(self):
        self._sounds = {"meow": "sounds/meow.wav"}

    def costumes(self):
        self._costumes = {
            "costume1": "sprites/cat.svg",
            "costume2": "sprites/g.png"
        }
        return self._costumes

if __name__ == "__main__":
    asyncio.run(Main().run())
```

---

## License

MIT © [Kian Metzsch](mailto:contact@ckm-tech.dev)

---

## Links

- [Homepage](https://github.com/k-metzsch/scrytch)
- [Issues](https://github.com/k-metzsch/scrytch/issues)
- [PyPI page](https://pypi.org/project/Scrytch/)
