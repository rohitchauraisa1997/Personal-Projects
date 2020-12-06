import pygame
import sys
import os
pygame.init()
print(sys.path)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("first game")
# initial position 
x,y = 50,50
# width and height of rectangle
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # to check which key was pressed.
    keys = pygame.key.get_pressed()

    # x>vel enables us to make sure that 
    # we dont move cursor out of LHS 
    # of the screen
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH-width-vel:
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel

    if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT-height-vel:
        y += vel

    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()
pygame.quit()
