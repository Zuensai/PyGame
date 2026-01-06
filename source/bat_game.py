import pygame
import sys
import os
from Bat import Bat
from pillar import Pillar

pygame.init()

# ------------------ Screen / Timing ------------------
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bat")
clock = pygame.time.Clock()

# ------------------ Game State ------------------
BG_COLOR = (84, 59, 230)
GROUND_Y = SCREEN_HEIGHT
CEILING_Y = 0

game_active = True
score = 0
highscore = 0

# ------------------ Paths ------------------
BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, "game-assets")

bat_path = os.path.join(ASSETS_DIR, "bat-1.png")
pillar_image_path = os.path.join(ASSETS_DIR, "pillar.png")
font_path = os.path.join(ASSETS_DIR, "Pixeltype.ttf")
highscore_file = os.path.join(BASE_DIR, "highscore.txt")

# ------------------ Highscore Load ------------------
if os.path.exists(highscore_file):
    try:
        with open(highscore_file, "r") as f:
            highscore = int(f.read())
    except:
        highscore = 0

# ------------------ Assets ------------------
if not os.path.exists(bat_path):
    print(f"ERROR: Missing bat image at {bat_path}")
    pygame.quit()
    sys.exit()

bat = Bat(100, 300, bat_path, scale=3)

if os.path.exists(font_path):
    game_font = pygame.font.Font(font_path, 40)
    game_over_font = pygame.font.Font(font_path, 70)
else:
    game_font = pygame.font.SysFont(None, 40)
    game_over_font = pygame.font.SysFont(None, 70)

# ------------------ Pillars ------------------
pillars = []

BASE_PILLAR_SPEED = 3
BASE_GAP_HEIGHT = 180
PILLAR_INTERVAL = 1500  # ms
last_pillar_time = pygame.time.get_ticks()

# ------------------ Helpers ------------------
def save_highscore():
    global highscore
    if score > highscore:
        highscore = score
        with open(highscore_file, "w") as f:
            f.write(str(highscore))

def reset_highscore():
    global highscore
    highscore = 0
    if os.path.exists(highscore_file):
        os.remove(highscore_file)

def check_collision():
    if bat.y < CEILING_Y or bat.y + bat.height > GROUND_Y:
        return True
    for pillar in pillars:
        if bat.rect.colliderect(pillar.top_rect) or bat.rect.colliderect(pillar.bottom_rect):
            return True
    return False

def reset_game():
    global score, game_active, last_pillar_time
    bat.y = 300
    bat.velocity = 0
    pillars.clear()
    score = 0
    game_active = True
    last_pillar_time = pygame.time.get_ticks()

# ------------------ Main Loop ------------------
def main():
    global score, game_active, last_pillar_time

    running = True

    while running:
        # ---------- Events ----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_highscore()
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bat.flap()

                elif event.key == pygame.K_r and not game_active:
                    reset_game()

                elif event.key == pygame.K_h:
                    reset_highscore()

        # ---------- Game Logic ----------
        if game_active:
            bat.update()

            pillar_speed = BASE_PILLAR_SPEED + score * 0.3
            gap_height = max(BASE_GAP_HEIGHT - score * 2, 100)

            now = pygame.time.get_ticks()
            if now - last_pillar_time > PILLAR_INTERVAL:
                pillars.append(
                    Pillar(
                        SCREEN_WIDTH,
                        SCREEN_HEIGHT,
                        image_path=pillar_image_path,
                        width=70,
                        gap_height=gap_height,
                        speed=pillar_speed
                    )
                )
                last_pillar_time = now

            for pillar in pillars:
                pillar.update()
                if not pillar.passed and bat.x > pillar.x + pillar.width:
                    pillar.passed = True
                    score += 1

            pillars[:] = [p for p in pillars if not p.off_screen()]

            if check_collision():
                game_active = False
                save_highscore()

        # ---------- Draw ----------
        screen.fill(BG_COLOR)

        for pillar in pillars:
            pillar.draw(screen)

        bat.draw(screen)

        score_text = game_font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        high_text = game_font.render(f"High Score: {highscore}", True, (255, 255, 0))
        screen.blit(high_text, (10, 50))

        reset_text = game_font.render("Reset with (h)", True, (255, 255, 255))
        screen.blit(reset_text, (10, 90))

        if not game_active:
            over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(over_text, over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)))

            retry_text = game_font.render("Press R to restart", True, (255, 255, 255))
            screen.blit(retry_text, retry_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30)))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# ------------------ Entry ------------------
if __name__ == "__main__":
    main()
