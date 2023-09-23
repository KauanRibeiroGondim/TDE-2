import pygame
import sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('TDE 2 Kauan')

white = (255, 255, 255)
red = (255, 0, 0)
x, y = 100, 100
velocidade = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(white)
    pygame.draw.rect(DISPLAYSURF, red, (x, y, 50, 50))

    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocidade
    if keys[pygame.K_RIGHT]:
        x += velocidade
    if keys[pygame.K_UP]:
        y -= velocidade
    if keys[pygame.K_DOWN]:
        y += velocidade

























