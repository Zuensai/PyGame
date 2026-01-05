import pygame
from pygame import Color
from pygame.locals import QUIT
import sys
from Bat import Bat
 
pygame.init() 


FPS = 60
clock = pygame.time.Clock()

WHITE = Color(255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600


DISPLAY_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("Game")


def main():
    running = True  
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()
        DISPLAY_SCREEN.fill(WHITE)

        pygame.display.update()
        

        clock.tick(FPS)
        


if __name__ == "__main__":
    main()
