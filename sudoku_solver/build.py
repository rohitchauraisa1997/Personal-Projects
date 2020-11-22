sample_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def validate_entry(board, num, pos):
    # pos is a tuple with first arg as row and second as column.
    # checking whether rows dont have duplicate entry
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # checking whether columns dont have duplicate entry
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # checking whether same 3*3 box doesnt have duplicate entry

    '''
    (0, 0) (0, 1) (0, 2) |  (0, 3) (0, 4) (0, 5) |  (0, 6) (0, 7) (0, 8) 

    (1, 0) (1, 1) (1, 2) |  (1, 3) (1, 4) (1, 5) |  (1, 6) (1, 7) (1, 8) 

    (2, 0) (2, 1) (2, 2) |  (2, 3) (2, 4) (2, 5) |  (2, 6) (2, 7) (2, 8) 
    - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - 
    (3, 0) (3, 1) (3, 2) |  (3, 3) (3, 4) (3, 5) |  (3, 6) (3, 7) (3, 8) 

    (4, 0) (4, 1) (4, 2) |  (4, 3) (4, 4) (4, 5) |  (4, 6) (4, 7) (4, 8) 

    (5, 0) (5, 1) (5, 2) |  (5, 3) (5, 4) (5, 5) |  (5, 6) (5, 7) (5, 8) 
    - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - 
    (6, 0) (6, 1) (6, 2) |  (6, 3) (6, 4) (6, 5) |  (6, 6) (6, 7) (6, 8) 

    (7, 0) (7, 1) (7, 2) |  (7, 3) (7, 4) (7, 5) |  (7, 6) (7, 7) (7, 8) 

    (8, 0) (8, 1) (8, 2) |  (8, 3) (8, 4) (8, 5) |  (8, 6) (8, 7) (8, 8) 


    1st box (0, 0)--> (0,0) (0,1) (0,2) (1,0) (1,1) (1,2) (2,0) (2,1) (2,2)
    2nd box (0, 1)--> (0,3) (0,4) (0,5) (1,3) (1,4) (1,5) (2,3) (2,4) (2,5)
    3rd box (0, 2)--> (0,6) (0,7) (0,8) (1,6) (1,7) (1,8) (2,6) (2,7) (2,8)
    4th box (1, 0)--> (3,0) (3,1) (3,2) (4,0) (4,1) (4,2) (5,0) (5,1) (5,2)
    5th box (1, 1)--> (3,3) (3,4) (3,5) (4,3) (4,4) (4,5) (5,3) (5,4) (5,5)
    6th box (1, 2)--> (3,6) (3,7) (3,8) (4,6) (4,7) (4,8) (5,6) (5,7) (5,8)
    7th box (2, 0)--> (6,0) (6,1) (6,2) (7,0) (7,1) (7,2) (8,0) (8,1) (8,2)
    8th box (2, 1)--> (6,3) (6,4) (6,5) (7,3) (7,4) (7,5) (8,3) (8,4) (8,5)
    9th box (2, 2)--> (6,6) (6,7) (6,8) (7,6) (7,7) (7,8) (8,6) (8,7) (8,8)
    '''
    # checking box
    box_x_cord = pos[1]//3
    box_y_cord = pos[0]//3
    for i in range (box_y_cord*3, box_y_cord*3 +3):
        for j in range (box_x_cord*3, box_x_cord*3 +3):
            if board[i][j] == num and (i,j)!= pos:
                return False

    return True
            
def print_sudoku_board(board):
    for i in range (len(board)):
        # print(i,end = " ")
        if i%3 ==0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j%3 ==0 and j != 0:
                print(" | ",end = "")
            print(board[i][j], end = " ")
            if j == len(board[0]) - 1:
                print("\n")

def find_empty_in_board(board):
    for i in range (len(board)):
        for j in range(len(board[0])):
            # print((i,j))
            if board[i][j] == 0:
                return(i,j) #row,column
    return None

def print_board_cords(board):
    for i in range (len(board)):
        for j in range (len(board[0])):
            print((i,j),end = " ")
            if j == len(board) - 1:
                print("\n")

def execute(board):
    print("\n\n")
    print_sudoku_board(board)
    print("\n\n")
    # first we find the empty row and column.
    find = find_empty_in_board(board)
    # if no empty found it returns True else we get
    # the row and column on which we need to work on.
    if not find:
        return True
    else:
        row, column = find
    
    # if we loop through all the numbers and none of them meet the condition
    # we return False
    for i in range(1,10):
    # now we check whether adding the number between 1 and 10 works.
        if validate_entry(board, i, (row,column)):
            board[row][column] = i
            # after we add the number to that row and column and then 
            # recursively call the execute function 
            if execute(board):
                return True
            # backtrack
            board[row][column] = 0
    
    return False

if __name__ == "__main__":
    print_sudoku_board(sample_board)
    execute(sample_board)
    print("++++++++++++++++++++++++++\n\n\n\n\n\n")
    print_sudoku_board(sample_board)
    for i in 10:
        print(i)