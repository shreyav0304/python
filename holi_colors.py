import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Holi Colors Splash")

COLORS = [
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
    (255, 192, 203),  # Pink
    (0, 255, 255)     # Cyan
]

running = True

def draw_splash(surface, position, size, color):
    for _ in range(size):
        offset_x = random.randint(-size, size)
        offset_y = random.randint(-size, size)
        radius = random.randint(1, 5)
        pygame.draw.circle(surface, color, (position[0] + offset_x, position[1] + offset_y), radius)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            color = random.choice(COLORS)
            draw_splash(screen, mouse_pos, size=50, color=color)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
