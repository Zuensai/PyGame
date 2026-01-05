import pygame
from pygame import Color
from pygame.locals import QUIT
import sys

 
pygame.init() 


FPS = 60
clock = pygame.time.Clock()


# Zet dit op False als je naar 'Game Over' screen wilt gaan.
game_active = True

WHITE = Color(255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600


# 'Game Over' tekst
game_font = pygame.font.Font('fonts\Pixeltype.ttf', 50)
game_over_text_surf = game_font.render("Game Over", False, ("#ffffff"))
game_over_text_rect = game_over_text_surf.get_rect(center= (200, 300))


DISPLAY_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("Game")


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        if game_active:
            DISPLAY_SCREEN.fill("#543be6")
        else: 
            DISPLAY_SCREEN.fill("#3c070e")
            DISPLAY_SCREEN.blit(game_over_text_surf, game_over_text_rect)



        pygame.display.update()
        clock.tick(FPS)
        


if __name__ == "__main__":
    main()
