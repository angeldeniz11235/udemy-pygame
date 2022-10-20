import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700, 700), 0, 32)
sprite1 = pygame.image.load('./images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (50, 50))
pygame.display.set_caption("Hello Sprite")
screen.fill((0, 0, 0))

[screen_height, screen_width] = screen.get_height(), screen.get_width()

[sprite1_height, sprite1_width] = sprite1.get_height(), sprite1.get_width()

game_over = False
x, y = (0, 0)
clock = pygame.time.Clock();

while not game_over:
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pressed = pygame.key.get_pressed()
    if pressed[K_UP] and y > 0:
        y -= 0.5 * dt
    elif pressed[K_DOWN] and (y + sprite1_height) < screen_height:
        y += 0.5 * dt
    elif pressed[K_RIGHT] and (x + sprite1_width) < screen_width:
        x += 0.5 * dt
    elif pressed[K_LEFT] and x > 0:
        x -= 0.5 * dt
    elif pressed[K_SPACE]:
        x = 0
        y = 0
    screen.fill((0, 0, 0))
    screen.blit(sprite1, (x, y))
    pygame.display.update()

pygame.quit()
