import pygame
import sys
from pygame.locals import QUIT
import math
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Rotação de Objeto')
white = (255, 255, 255)
red = (255, 0, 0)
rotation_point = (200, 200)
angle = 0 
angular_velocity = 2  
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(white)
    width, height = 100, 50
    x1 = rotation_point[0] - width / 2
    y1 = rotation_point[1] - height / 2
    x2 = rotation_point[0] + width / 2
    y2 = rotation_point[1] - height / 2
    x3 = rotation_point[0] + width / 2
    y3 = rotation_point[1] + height / 2
    x4 = rotation_point[0] - width / 2
    y4 = rotation_point[1] + height / 2
    rotated_x1 = rotation_point[0] + (x1 - rotation_point[0]) * math.cos(math.radians(angle)) - (y1 - rotation_point[1]) * math.sin(math.radians(angle))
    rotated_y1 = rotation_point[1] + (x1 - rotation_point[0]) * math.sin(math.radians(angle)) + (y1 - rotation_point[1]) * math.cos(math.radians(angle))
    rotated_x2 = rotation_point[0] + (x2 - rotation_point[0]) * math.cos(math.radians(angle)) - (y2 - rotation_point[1]) * math.sin(math.radians(angle))
    rotated_y2 = rotation_point[1] + (x2 - rotation_point[0]) * math.sin(math.radians(angle)) + (y2 - rotation_point[1]) * math.cos(math.radians(angle))
    rotated_x3 = rotation_point[0] + (x3 - rotation_point[0]) * math.cos(math.radians(angle)) - (y3 - rotation_point[1]) * math.sin(math.radians(angle))
    rotated_y3 = rotation_point[1] + (x3 - rotation_point[0]) * math.sin(math.radians(angle)) + (y3 - rotation_point[1]) * math.cos(math.radians(angle))
    rotated_x4 = rotation_point[0] + (x4 - rotation_point[0]) * math.cos(math.radians(angle)) - (y4 - rotation_point[1]) * math.sin(math.radians(angle))
    rotated_y4 = rotation_point[1] + (x4 - rotation_point[0]) * math.sin(math.radians(angle)) + (y4 - rotation_point[1]) * math.cos(math.radians(angle))
    pygame.draw.polygon(DISPLAYSURF, red, [(rotated_x1, rotated_y1), (rotated_x2, rotated_y2), (rotated_x3, rotated_y3), (rotated_x4, rotated_y4)])
    pygame.display.update()
    angle += angular_velocity
    pygame.time.Clock().tick(60)
