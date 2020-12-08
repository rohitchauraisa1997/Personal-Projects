import os
import pygame
from grid import Grid

os.environ["SDL_VIDEO_WINDOW_POS"] = "100,100"
surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("TIC_TAC_TOE")

running = True
grid = Grid()
player = "X"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            # print((pygame.mouse.get_pressed()))
            # pygame.mouse.get_pressed()
            # returns a tuple of 3 values
            # depending on which button was clicked.
            # left,middle,right
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                """
				(00),(10),(20)
				(01),(11),(21)
				(02),(12),(22)
				"""
                # print(pos[0]//200,pos[1]//200)
                grid.get_mouse(pos[0] // 200, pos[1] // 200, player)
                # alternating chances.
                if grid.switch_player:
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"
                grid.print_grid()
                print("\n")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False

            if event.key == pygame.K_ESCAPE:
                running = False
    # RGB
    surface.fill((0, 0, 0))
    grid.draw(surface)
    pygame.display.flip()
