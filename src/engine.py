import pygame
import sys

class Engine:
    def __init__(self, game_logic, width, height, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.window_size = (width, height)
        self.screen = pygame.display.set_mode(self.window_size)        
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_logic = game_logic
        self._first_loop = True
        self.sprites = self.sprites()

    def run(self, fps=60):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            for sprite in self.sprites:
                sprite.events()

            self.screen.fill((255, 255, 255))

            for sprite in self.sprites:
                sprite._draw(self.screen)

            pygame.display.flip()
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()