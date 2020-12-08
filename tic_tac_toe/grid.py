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
        # search directions N       NW     W      SW     S      SE     E      NE
        self.search_dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

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
            # iside if so check_grid only runs when 
            # get_cell_Value encounters 0
            self.check_grid(x,y,player)
        else:
            self.switch_player = False

    def is_withhin_bounds(self,x,y):
        return x >=0 and  x<3 and y>=0 and y<3
    
    # bound_check.png
    '''
    considering this location first it goes for N dir
    since is_within_bounds fails as y=-1
    then we go for NW direction as y = -1
    then we go for W direction it is successful as x+dirx = 1
    '''
    def check_grid(self,x,y,player):
        count = 1

        for index, (dirx,diry) in enumerate(self.search_dirs):
            count = 1
            # success_implemetation
            '''
            considering this image we go through each direction for 
            X in (0,2) coordinate and when we encounter NE direction 
            we find with self.get_cell_value == player hence we increase
            count to 2 similarily in the next nested if count becomes 3
            '''
            if self.is_withhin_bounds(x+dirx, y+diry) and self.get_cell_value(x+dirx,y+diry) == player:
                # increasing count to 2
                count += 1
                xx = x + dirx
                yy = y + diry
                if self.is_withhin_bounds(xx+dirx, yy+diry) and self.get_cell_value(xx+dirx,yy+diry) == player:
                    # increasing count to 3
                    count += 1
                    if count == 3:
                        break
                
                if count < 3: 
                    # need_to_reverse.png
                    '''
                    considering this case we will have count = 3
                    hence we need to reverse direction.
                    '''
                    new_dir = 0
                    #reverse.png
                    '''
                    considering this case we reverse the dir from SW to NE
                    '''
                    if index == 0:
                        new_dir = self.search_dirs
                        new_dir = self.search_dirs[4] # N to S
                    elif index == 1:
                        new_dir = self.search_dirs[5] # NW to SE
                    elif index == 2:
                        new_dir = self.search_dirs[6] # W to E
                    elif index == 3:
                        new_dir = self.search_dirs[7] # SW to NE
                    elif index == 4:
                        new_dir = self.search_dirs[0] # S to N
                    elif index == 5:
                        new_dir = self.search_dirs[1] # SE to NW
                    elif index == 6:
                        new_dir = self.search_dirs[2] # E to W
                    elif index == 7:
                        new_dir = self.search_dirs[3] # NE to SW

                    if self.is_withhin_bounds(x+new_dir[0], y+new_dir[1]) and self.get_cell_value(x+new_dir[0], y=new_dir[1])==player:
                        count += 1
                        if count == 3:
                            break
                    else:
                        count = 1

        if count == 3:
            print(player,"wins")
            return

    def print_grid(self):
        for row in self.grid:
            print(row)
    