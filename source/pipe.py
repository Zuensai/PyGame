import os
import pygame
import random

class Pipe:
    MOVEMEND_SPEED: float = 10

    def __init__(self, screen_width: int, screen_height: int):
        self.image = pygame.image.load(os.path.join("game-assets", "pillar.png"))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = screen_width - 20
        self.hitbox.y = 0
        self.hitbox.height = random.randint(int(screen_height * 0.1), int(screen_height * 0.5))

    def update(self, delta: float):
        self.hitbox.x -= int(Pipe.MOVEMEND_SPEED * delta)

    def draw(self, surface: pygame.Surface):
        surface.blit(pygame.transform.scale(self.image, self.hitbox.size), self.hitbox)
