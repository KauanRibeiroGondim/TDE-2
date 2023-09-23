import pygame
import sys
from pygame.locals import QUIT
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Escala de Objeto')
white = (255, 255, 255)
red = (255, 0, 0)
scale_point = (200, 200)
width, height = 100, 50
scale_factor = 2.0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(white)
    x1 = scale_point[0] - width / 2
    y1 = scale_point[1] - height / 2
    x2 = scale_point[0] + width / 2
    y2 = scale_point[1] - height / 2
    x3 = scale_point[0] + width / 2
    y3 = scale_point[1] + height / 2
    x4 = scale_point[0] - width / 2
    y4 = scale_point[1] + height / 2
    scaled_x1 = scale_point[0] + (x1 - scale_point[0]) * scale_factor
    scaled_y1 = scale_point[1] + (y1 - scale_point[1]) * scale_factor
    scaled_x2 = scale_point[0] + (x2 - scale_point[0]) * scale_factor
    scaled_y2 = scale_point[1] + (y2 - scale_point[1]) * scale_factor
    scaled_x3 = scale_point[0] + (x3 - scale_point[0]) * scale_factor
    scaled_y3 = scale_point[1] + (y3 - scale_point[1]) * scale_factor
    scaled_x4 = scale_point[0] + (x4 - scale_point[0]) * scale_factor
    scaled_y4 = scale_point[1] + (y4 - scale_point[1]) * scale_factor
    pygame.draw.polygon(DISPLAYSURF, red, [(scaled_x1, scaled_y1), (scaled_x2, scaled_y2), (scaled_x3, scaled_y3), (scaled_x4, scaled_y4)])
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        scale_factor += 0.5 
    elif keys[pygame.K_DOWN]:
        scale_factor -= 0.5 
