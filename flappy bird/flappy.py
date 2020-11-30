import time
import os
import random
import pygame
import neat

WIN_WIDTH = 600
WIN_HEIGHT = 800
print("********")
print(os.getcwd())
print(os.path.join("images", "bird1.png"))
print("********")
BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png"))),
]

PIPE_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join("images", "pipe.png"))
)

BASE_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join("images", "base.png"))
)

BG_IMG = pygame.transform.scale2x(
    pygame.image.load(os.path.join("images", "bg.png"))
)

class Bird:
    IMGS = BIRD_IMGS
    # how much bird tilts while moving up and down
    MAX_ROTATION = 25
    # how much we rotate on each frame 
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        # starting pos of our bird
        self.x = x
        self.y = y
        # how much the image is tilted initialised
        # by 0 since its flat in the beginning.
        self.tilt = 0
        # defines the physics related to that 
        # particular bird 
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]
    
    def jump(self):
        #called when we need
        #the bird to flap up
        #-ve velocity enables us to jump up
        #(0,0) is the top lhs cordinate
        self.vel = -10.5
        #keeps track of when we last jumped
        #set tick_count = 0 for every jump
        self.tick_count = 0
        #where the bird jumped from
        self.height = self.y

    def move(self):
        #move() enables the bird to move
        self.tick_count += 1 
        # displacement tells us how much we move up or how much we move down
        # tick_count tells us how much time we r moving for
        d = self.vel*self.tick_count + 1.5*self.tick_count**2
        #for tick_count = 1 ; -10.5*1 + 1.5*1**2 = -10.5 + 1.5 = -9 ----> moving 9 pixels upwards
        #for tick_count = 2 ; -10.5*2 + 1.5*2**2 = -21 + 6 = -15 ----> moving 9 pixels upwards
        
        # if we r moving down more than 16 just move 16
        if d>=16:
            d = 16
        
        #fine tunes the movement
        #d<0 implies we r moving upwards
        if d<0:
            d -= 2

        self.y = self.y + d

        if d<0 or self.y < slef.height + 50:
            