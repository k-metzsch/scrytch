import pygame
import sys

class Scrython:
    def __init__(self, game_logic, width, height, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.window_size = (width, height)
        self.screen = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_logic = game_logic
        
        # Initialize sprites, costumes, and backdrops
        self.sprites = self.sprites()
        self.costumes = self.costumes()
        self.backdrops = self.backdrops()
        
        self.background_image = (None, None)
            
    
    def _set_backdrop(self, backdrop_name, backdrop_path):
        self.background_image = (backdrop_name, pygame.image.load(backdrop_path).convert())

    def run(self, fps=60):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Call logic for all sprites
            for sprite in self.sprites:
                sprite.events()

            # Draw background
            if self.background_image and self.background_image[1]:
                self.screen.blit(self.background_image[1], (0, 0))
            else:
                self.screen.fill((255, 255, 255))

            # Draw all sprites
            for sprite in self.sprites:
                sprite._draw(self.screen)
                sprite._draw_bubble(self.screen)

            pygame.display.flip()
            self.clock.tick(fps)
        pygame.quit()
        sys.exit()