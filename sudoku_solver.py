import copy
"""
def valid(board):
    \"""
    Takes a sudoku board and returns true if the board follows the rules of 9x9 sudoku
    \"""
    ret = True
    for row in board:
        if sum(row) != 45:
            ret = False
        if len(set(row)) != len(row):
            ret = False

    col_sum= 0
    col_set= set()
    for i in range(9):
        for col in board:
            col_sum += col[i]
            col_set.add(col[i])
        if col_sum != 45:
            ret = False
        if len(col_set)!=9:
            ret = False
        col_sum=0
        col_set.clear()
    
    block1=[]
    block2=[]
    block3=[]
    for row in board:
        if len(block1) == 9:
            if sum(block1)!=45:
                ret=False
            if sum(block2)!=45:
                ret=False
            if sum(block3)!=45:
                ret=False
            block1.clear()
            block2.clear()
            block3.clear()
    
        block1.extend([row[0],row[1],row[2]])
        block2.extend([row[3],row[4],row[5]])
        block3.extend([row[6],row[7],row[8]])
    return ret
"""

def print_grid(arr):
    """
    Prints a sudoku board separated by spaces
    :param arr: 2D list of int
    :return: None
    """
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=' ')
        print('\n')
    

def check_row(board, num, row):
    """
    Checks if a specified num on specified row on sudoku board is safe
    :param board: 2D list of int
    :param num: int
    :param row: list of int
    """
    for i in range(9):
        if board[row][i] == num:
            return False
    return True

def check_col(board, num, col):
    """
    Checks if a specified num on specified column on sudoku board is safe
    :param board: 2D list of int
    :param num: int
    :param col: list of int
    """
    for i in range(9):
        if board[i][col] == num:
            return False
    return True

def check_box(board, num, row, col):
    """
    Checks if a specified num a subsection of sudoku board is safe
    :param board: 2D list of int
    :param num: int
    :param row: list of int
    :param col: list of int
    """
    for i in range(3):
        for j in range(3):
            if board[row-(row%3)+i][col-(col%3)+j] == num:
                return False
    return True

def check_safe(board, num, row, col):
    """
    Checks if num is safe in specified row, column, and subsection box
    :param board: 2D list of int
    :param num: int
    :param row: list of int
    :param col: list of int
    """
    return check_row(board, num, row) and \
            check_col(board, num, col) and \
            check_box(board, num, row, col)

def find_empty_space(board):
    """
    Checks for next empty space in the board, -1,-1 if there is no empty space
    :param board: 2D list of int
    return coords: list of int
    """
    coords = [-1, -1]
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                coords[0] = i
                coords[1] = j
    return coords



def idliketosolvethepuzzle(board):
    coords = find_empty_space(board)
    if coords == [-1, -1]:
        return True
    for i in range(1, 10):
        if check_safe(board, i, coords[0], coords[1]):
            board[coords[0]][coords[1]] = i
            if idliketosolvethepuzzle(board):
                return True
            board[coords[0]][coords[1]] = 0
    return False

def multiple_solutions(board, count, l):
    coords = find_empty_space(board)
    if coords == [-1, -1]:
        return 1+count
    for i in range(1, 10):
        if check_safe(board, i, coords[0], coords[1]):
            board[coords[0]][coords[1]] = i
            count = multiple_solutions(board, count, l)
    board[coords[0]][coords[1]] = 0
    return count


b = [
    [8,0,0,0,0,7,5,4,0],
    [0,0,6,0,0,0,3,0,0],
    [3,5,0,0,0,0,2,0,1],
    [0,0,0,6,0,0,0,1,0],
    [5,7,0,1,8,4,0,0,0],
    [9,6,0,0,0,5,0,0,0],
    [0,0,3,0,6,0,0,0,7],
    [0,1,0,8,0,0,6,0,0],
    [0,0,4,5,0,9,0,0,2]
]
solved = [
    [6,8,4,1,5,9,7,3,2],
    [7,5,1,8,3,2,9,4,6],
    [9,2,3,6,7,4,1,8,5],
    [1,9,2,3,6,5,8,7,4],
    [8,4,5,2,1,7,6,9,3],
    [3,6,7,4,9,8,2,5,1],
    [2,3,9,7,4,6,5,1,8],
    [5,1,6,9,8,3,4,2,7],
    [4,7,8,5,2,1,3,6,9]
]
solved2 = [
    [7,4,9,6,1,3,8,2,5],
    [8,6,1,4,5,2,9,3,7],
    [2,5,3,8,7,9,6,4,1],
    [4,3,2,7,6,8,1,5,9],
    [5,7,6,1,9,4,3,8,2],
    [9,1,8,3,2,5,4,7,6],
    [6,8,7,5,4,1,2,9,3],
    [3,2,5,9,8,6,7,1,4],
    [1,9,4,2,3,7,5,6,8]
]
unsolvable= [
    [0,0,9,0,2,8,7,0,0],
    [8,0,6,0,0,4,0,0,5],
    [0,0,3,0,0,0,0,0,4],
    [6,0,0,0,0,0,0,0,0],
    [0,2,0,7,1,3,4,5,0],
    [0,0,0,0,0,0,0,0,2],
    [3,0,0,0,0,0,5,0,0],
    [9,0,0,4,0,0,8,0,7],
    [0,0,1,2,5,0,3,0,0]
]
t= [
    [0,0,3,0,0,0,0,0,6],
    [0,0,0,9,8,0,0,2,0],
    [9,4,2,6,0,0,7,0,0],
    [4,5,0,0,0,6,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [1,0,9,0,5,0,4,7,0],
    [0,0,0,0,2,5,0,4,0],
    [6,0,0,0,7,8,5,0,0],
    [0,0,0,0,0,0,0,0,0]
]
# t_copy=copy.deepcopy(b)
# if idliketosolvethepuzzle(b) and multiple_solutions(t_copy,0,[]) <=1:
#     print_grid(b)
# else:
#     print("no solution")