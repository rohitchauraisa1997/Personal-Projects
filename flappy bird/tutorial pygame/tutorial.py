import pygame
import sys
import os
pygame.init()
print(sys.path)
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("first game")
x,y = 50,50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
pygame.quit()
