import pygame
import random
import os

class Pillar:
    def __init__(self, x, screen_height, image_path=None, width=50, gap_height=150, speed=3):
        self.x = x
        self.width = width
        self.gap_height = gap_height
        self.speed = speed
        self.screen_height = screen_height

        # Random gap position
        self.gap_y = random.randint(100, screen_height - 100 - gap_height)

        # Collision rects
        self.top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        self.bottom_rect = pygame.Rect(self.x, self.gap_y + self.gap_height, self.width, screen_height - (self.gap_y + self.gap_height))

        # Optional image
        if image_path and os.path.exists(image_path):
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.screen_height))
        else:
            self.image = None

        self.passed = False  # For scoring

    def update(self):
        self.x -= self.speed
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        if self.image:
            # Draw top pillar
            top_image = pygame.transform.scale(self.image, (self.width, self.gap_y))
            screen.blit(top_image, (self.x, 0))
            # Draw bottom pillar
            bottom_height = self.screen_height - (self.gap_y + self.gap_height)
            bottom_image = pygame.transform.scale(self.image, (self.width, bottom_height))
            screen.blit(bottom_image, (self.x, self.gap_y + self.gap_height))
        else:
            # Fallback to green rectangles
            pygame.draw.rect(screen, (0, 255, 0), self.top_rect)
            pygame.draw.rect(screen, (0, 255, 0), self.bottom_rect)

    def off_screen(self):
        return self.x + self.width < 0
