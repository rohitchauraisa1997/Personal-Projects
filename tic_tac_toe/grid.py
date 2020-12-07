import os
import pygame

letter_X = pygame.image.load(os.path.join('images','X_modified.png'))
letter_O = pygame.image.load(os.path.join('images','o_modified.png'))
class Grid:
    def __init__(self):
        self.grid_lines = [((0,200),(600,200)),#first horizontal line
                           ((0,400),(600,400)),#second horizontal line
                           ((200,0),(200,600)),#first vertical line
                           ((400,0),(400,600))]#second vertical line
    
        self.grid = [[0 for x in range(3)]for y in range(3)]
        self.switch_player = True

    def draw(self,surface):
        for line in self.grid_lines:
            # surface: Surface,color: _ColorValue,start_pos: _Coordinate,end_pos: _Coordinate,width: Optional[int] = 1,
            pygame.draw.line(surface,(200,200,200),line[0],line[1],2)
        
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x,y) == "X":
                    surface.blit(letter_X, (x*200, y*200))
                elif self.get_cell_value(x,y) == "O":
                    surface.blit(letter_O, (x*200, y*200))

    def get_cell_value(self,x,y):
        return self.grid[y][x]

    def set_cell_value(self,x,y,value):
        self.grid[y][x] = value

    def get_mouse(self,x,y,player):
        # done to prevent overwriting
        if self.get_cell_value(x,y) == 0:
            # EDGE CASE
            # created self.switch_player 
            # to prevent repeated chances 
            # created during prevention of overwriting
            self.switch_player = True
            if player == "X":
                self.set_cell_value(x,y,"X")
            elif player == "O":
                self.set_cell_value(x,y,"O")
        else:
            self.switch_player = False

    def print_grid(self):
        for row in self.grid:
            print(row)
    