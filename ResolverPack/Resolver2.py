import random


def Solver2(grid):

    inGrid = ClassifyGrid3(grid)

    count = 0

    for l in range(9):
        for c in range(9):

            if not inGrid[l][c]:

                grid[l][c] = random.randint(1,9)

            else:
                count += 1

    VerifyGrid(grid, inGrid)

    return count



def VerifyGrid(grid, inGrid):

    for l in range(9):
        for c in range(9):

            if not inGrid[l][c]:
                VerifyNumber(inGrid, grid, l, c)




def VerifyNumber(inGrid, grid, l, c):

    isValid = True

    for i in range(9):    #verif ligne / colonne

        if grid[i][c] == grid[l][c] and i != l:

            isValid = False

            if inGrid[i][c] == 0:
                grid[i][c] = 0


        if grid[l][i] == grid[l][c] and i != c:

            isValid = False

            if inGrid[l][i] == 0:
                grid[l][i] = 0

    l_c = int(l / 3) * 3
    c_c = int(c / 3) * 3

    for i in range(l_c, l_c + 3):     #verif case
        for j in range(c_c, c_c + 3):

            if i != l and j != c:

                if grid[i][j] == grid[l][c]:

                    isValid = False

                    if inGrid[i][j] == 0:
                        grid[i][j] = 0

    if not isValid:
        grid[l][c] = 0





def ClassifyGrid(grid):  # Transforme la grille en grille de vecteurs en fonction des valeurs dejà présente

    grid2 = []

    for l in range(9):
        for c in range(9):

            if grid[l][c] == 0:  # case vide

                case = [0, 0]
                grid2.append(case)

            else:
                case = [1, grid[l][c]]
                grid2.append(case)

    return grid2

def ClassifyGrid2(grid):  # Transforme la grille en grille de vecteurs en fonction des valeurs dejà présente

    grid2 = [[[0 for x in range(9)] for y in range(9)]for z in range(2)]

    for l in range(9):
        for c in range(9):

            if grid[l][c] == 0:  # case vide

                grid2[l][c][0] = 0
                grid2[l][c][1] = 0


            else:
                grid2[l][c][0] = 1
                grid2[l][c][1] = grid[l][c]

    return grid2

def ClassifyGrid3(grid):  # Transforme la grille en grille de vecteurs en fonction des valeurs dejà présente

    grid2 = [[0 for x in range(9)] for y in range(9)]

    for l in range(9):
        for c in range(9):

            if grid[l][c] == 0:  # case vide

                grid2[l][c] = False

            else:
                grid2[l][c] = True

    return grid2