import pygame

class Bat:
    def __init__(self, x, y, image_path, scale=3):
        image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(
            image,
            (image.get_width() * scale, image.get_height() * scale)
        )

        self.x = x
        self.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocity = 0
        self.gravity = 0.5
        self.flap_strength = -7
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def flap(self):
        self.velocity = self.flap_strength

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
