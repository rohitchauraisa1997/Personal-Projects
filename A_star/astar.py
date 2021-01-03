import math
import pygame
from queue import PriorityQueue
import pretty_errors

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Path Findig")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
# astar_algo.png
# a_starexplaination_of_heuristic_logic.png

class Spot:
    """
    Spot class handles the position of the spot in the
    grid,the color scheme of the visualisation on 
    which astar algo will work on.
    """    
    def __init__(self,row,col,width,total_rows):
        '''
        row --> row in which the spot should be made
        col --> column in which the spot should be made
        width --> width of the spot
        total_rows --> total rows in grid
        x,y define the postion of the spot in the grid.
        
        '''
        self.row = row
        self.col = col
        self.x = row * width
        self.y   = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    def get_post(self):
        return self.row,self.col

    def is_closed(self):
        #checks whether this node is in the closed set or not.
        # if the color is red we have already visited it and it fails.
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == PURPLE
    
    def reset(self):
        self.color = WHITE
        
    def make_open(self):
        self.color = GREEN
        
    def make_barrier(self):
        self.color = BLACK
        
    def make_end(self):
        self.color = TURQUOISE
    
    def make_path(self):
        self.color = PURPLE
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
        
    def make_start(self):
        self.color = ORANGE
    
    def update_neighbor(self,grid):
        pass
    
    def __lt__(self,other):
        # compares spot objects
        # lessthan
        return False
    
def h(p1,p2):
    # manhattan distance
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2)+abc(y1-y2)

def make_grid(rows,width):
    grid = []
    # tells us what the width of each cube should be.
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i,j,gap,rows)
            grid[i].append(spot)
    
    return grid
    
def draw_grid(win, rows, width):
    # drwaes the grid lines.
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()

def get_pos_clicked(pos, rows, width):
    # tells the position of the spot that got clicked.
    gap = width // rows
    y,x = pos
    
    row = y // gap
    col = x // gap
    return row, col

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)
    
    start = None
    end = None
    
    run = True
    started = False
    
    while run:
        draw(win,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if started:
                # prohibits user from doing anything 
                # once the a star algo starts running.
                continue
            
            # Left Mouse Button
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row,col = get_pos_clicked(pos,ROWS,width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                    
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                
                # making barriers
                elif spot != end and spot != start:
                    spot.make_barrier()
                    
            # Right Mouse Button
            elif pygame.mouse.get_pressed()[2]:
                # print("abc")
                pos = pygame.mouse.get_pos()
                row,col = get_pos_clicked(pos,ROWS,width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
                
            
    pygame.quit()
    
if __name__ == "__main__":
    main(WIN,WIDTH)