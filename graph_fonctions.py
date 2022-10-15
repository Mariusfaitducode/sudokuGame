import time

from ResolverPack.Resolver import *

TAB_GAP = 100

COTE_CASE = 50
NB_LINE = 9
LINE_WIDTH = 2
COTE_TAB = COTE_CASE * NB_LINE + 5


def draw_grid(cnv):
    # Dessin plateau
    for i in range(0, NB_LINE + 1):

        if i % 3 == 0:
            w = 5
        else:
            w = 2

        x1 = 4 + i * COTE_CASE
        x2 = x1
        y1 = 0
        y2 = COTE_TAB + 1

        cnv.create_line(x1, y1, x2, y2, width=w, fill='black')

        y1 = 4 + i * COTE_CASE
        y2 = y1
        x1 = 0
        x2 = COTE_TAB

        cnv.create_line(x1, y1, x2, y2, width=w, fill='black')


def init_grid(cnv, grid):
    # Placer le texte
    for i in range(NB_LINE):
        for j in range(NB_LINE):

            # w = 3 + int(i / 3)
            # w2 = 3 + int(j / 3)

            x = COTE_CASE / 2 + 5 + j * COTE_CASE
            y = COTE_CASE / 2 + 5 + i * COTE_CASE

            if grid[i][j] != 0:
                cnv.create_text(x, y, text=grid[i][j], fill='black', font='Helvetica 15 bold')


def show_final_grid(cnv, grid, grid2):
    for i in range(NB_LINE):
        for j in range(NB_LINE):

            # w = 3 + int(i / 3)
            # w2 = 3 + int(j / 3)

            x = COTE_CASE / 2 + 5 + j * COTE_CASE
            y = COTE_CASE / 2 + 5 + i * COTE_CASE

            if not grid2[i][j]:
                cnv.create_text(x, y, text=grid[i][j], fill='red', font='Helvetica 15 bold')


def resolver_button(cnv, grid):
    grid2 = ClassifyGrid3(grid)
    SolverGraph(grid, cnv)
    #Solver(grid)
    #show_final_grid(cnv, grid, grid2)


def SolverGraph(grid, cnv):

    l, c = FindCase(grid)

    if l == None :
        return True

    else:
        for var in range(1, 10):

            if AddNumber(var, grid, l, c):
                grid[l][c] = var

                x = COTE_CASE / 2 + 5 + c * COTE_CASE
                y = COTE_CASE / 2 + 5 + l * COTE_CASE


                cnv.create_text(x, y, text=grid[l][c], fill='black', font='Helvetica 15 bold')
                cnv.update()



                if SolverGraph(grid, cnv):
                    return True
                else:
                    grid[l][c] = 0

                    cnv.create_rectangle(x - 20, y - 20, x + 20, y + 20, fill="light gray", width= 0)
                    #cnv.update()


    return False


def ClassifyGrid3(grid):
    grid2 = [[0 for x in range(9)] for y in range(9)]

    for l in range(9):
        for c in range(9):

            if grid[l][c] == 0:  # case vide

                grid2[l][c] = False

            else:
                grid2[l][c] = True

    return grid2
