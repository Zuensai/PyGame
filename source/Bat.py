import pygame

class Bat:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocity = 0
        self.gravity = 0.5
        self.flap_strength = -10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def flap(self):
        """Make the bat go up."""
        self.velocity = self.flap_strength

    def update(self):
        """Apply gravity and update position."""
        self.velocity += self.gravity
        self.y += self.velocity

        # Update collision box
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """Draw the bat on the screen."""
        screen.blit(self.image, (self.x, self.y))
