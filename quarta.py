import pygame
import sys
from pygame.locals import QUIT
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Reflexão de Objeto')
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
reflection_point = (200, 200)
width, height = 100, 50
reflect_x = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(white)
    x1 = reflection_point[0] - width / 2
    y1 = reflection_point[1] - height / 2
    x2 = reflection_point[0] + width / 2
    y2 = reflection_point[1] - height / 2
    x3 = reflection_point[0] + width / 2
    y3 = reflection_point[1] + height / 2
    x4 = reflection_point[0] - width / 2
    y4 = reflection_point[1] + height / 2
    if reflect_x:
        x1 = 2 * reflection_point[0] - x1
        x2 = 2 * reflection_point[0] - x2
        x3 = 2 * reflection_point[0] - x3
        x4 = 2 * reflection_point[0] - x4
    for i in range(int(width)):
        for j in range(int(height)):
            if (i + j) % 2 == 0:
                pygame.draw.rect(DISPLAYSURF, red, (x1 + i, y1 + j, 1, 1))
            else:
                pygame.draw.rect(DISPLAYSURF, black, (x1 + i, y1 + j, 1, 1))
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        reflect_x = not reflect_x
