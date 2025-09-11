import pygame
import asyncio

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

    async def run(self, fps=60):
        for sprite in self.sprites:
            if hasattr(sprite, "events"):
                coro = getattr(sprite, "events")
                if asyncio.iscoroutinefunction(coro):
                    await coro()
                else:
                    coro()

        frame_delay = 1.0 / float(fps) if fps else 0

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Get logic from event in all sprites
            for sprite in self.sprites:
                if hasattr(sprite, "events"):
                    fn = getattr(sprite, "events")
                    if asyncio.iscoroutinefunction(fn):
                        await fn()
                    else:
                        fn()

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
            if frame_delay:
                await asyncio.sleep(frame_delay)
        pygame.quit()
        return