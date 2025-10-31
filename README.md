# Scrytch

**Scrytch** is a Python project that imitates Scratch game logic, making it easier to create interactive games and animations using Python. Built on top of [pygame](https://www.pygame.org/), Scrytch provides a simple API for sprites, backdrops, sounds, and is more ideal for educational projects, prototypes, or anyone who loves the Scratch workflow but wants to use Python.

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
from Scrytch.scrytch import Scrytch

class Main(Scrytch):
    def __init__(self, title="Scrython"):
        self.width=800
        self.height=600
        Scrytch.__init__(self, self, self.width, self.height, title)

    def sprites(self):
        # Sprites goes here
        self.cat1 = Cat1(self)
        return [
            self.cat1
        ]

    def backdrops(self):
        # Backdrops goes here
        self._backdrops = {
            "backdrop1": "backdrops/backdrop1.jpg",
        }
        return self._backdrops

    def sounds(self):
        # Sounds goes here
        self._sounds = {
            "meow": "sounds/meow.wav",
        }

    def costumes(self):
        # Costumes for sprites goes here
        self._costumes = {
            "costume1": "sprites/cat.svg",
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
