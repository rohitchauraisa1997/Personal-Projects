import time
import os
import random
import pygame
import neat
import os
# pygame.init()
os.environ["SDL_VIDEODRIVER"] = "dummy"
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

        if d<0 or self.y < self.height + 50:
            # tilting the bird upwards
            # we check if the position of bird is
            # above the position where bird jumped from
            # if it is then it means that we still r 
            # moving upwards so dont start falling down yet
            # as soon as we get below the point where we jumped from
            # we can start tilting the bird downwards.
            if self.tilt < self.MAX_ROTATION:
                # so rather than moving it up slowly
                # we can instantly change the tilt because 
                # tilt isnt that big
                self.tilt = self.MAX_ROTATION
        else:
            #tilting the bird downwards
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
    
    def draw(self,win):
        # img_count enables us to keep count of
        # how many times has the bird appeared
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0
        
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2
        
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x,self.y)).center)
        win.blit(rotated_image, new_rect.topleft)
    
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

def draw_window(win, bird):
    win.blit(BG_IMG,(0,0))
    bird.draw(win)
    pygame.display.update()

def main():
    # pass
    bird = Bird(200,2000)
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(win,bird)
    
    pygame.quit()
    quit()

main()