

import numpy as np

def EnterGrid():

    print("Entrer votre grille")

    grid = np.array([list(map(int, input())) for _ in range(9)])

    for i in grid:
        print(''.join(map(str, i)))


def Solver(grid):


    l, c = FindCase(grid)

    if l == None :
        return True

    else:
        for var in range(1, 10):

            if AddNumber(var, grid, l, c):
                grid[l][c] = var
                if Solver(grid):
                    return True
                else:
                    grid[l][c] = 0

    return False

def AddNumber(var, grid, l, c):

    for i in range(9):    #verif ligne / colonne

        if grid[i][c] == var:
            return False

        if grid[l][i] == var:
            return False

    l_c = int(l / 3) * 3
    c_c = int(c / 3) * 3

    for i in range(l_c, l_c + 3):     #verif case
        for j in range(c_c, c_c + 3):

            if grid[i][j] == var:
                return False

    return True


def FindCase(grid):

    for l in range(9):
        for c in range(9):

            if grid[l][c] == 0:  # case vide
                return l, c

    return None, None

def PrintSudoku(puzzle):
    """Prints the sudoku board"""
    print("+" + "---+" * 9)
    for i, row in enumerate(puzzle):
        print(("|" + " {}   {}   {} |" * 3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+" * 9)
        else:
            print("+" + "   +" * 9)


