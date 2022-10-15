import random


def InitGrid(grid, inGrid):

    for i in range (3):
        for j in range (3):

            x = i * 3
            y = j * 3

            FillGrid(inGrid, grid, x, y)

def FillGrid(inGrid, grid, i, j):     #remplie grille 3*3

    list = []

    for l in range(i, i + 3):
        for c in range(j, j + 3):

            if inGrid[l][c]:

                list.append(grid[l][c])

    for l in range(i, i + 3):
        for c in range(j, j + 3):

            if not inGrid[l][c]:

                valid = False
                var = 0
                while not valid:

                    valid = True
                    var = random.randint(1,9)

                    for i in list:
                        if i == var:
                            valid = False

                grid[l][c] = var
                list.append(var)



def Solver3(grid):

    inGrid = ClassifyGrid3(grid)

    InitGrid(grid, inGrid)

    PrintSudoku(grid)

    lignError, columnError = CountError(grid)

    listErrorGrid = ClassifyError(lignError, columnError)

    total = TotalError(listErrorGrid)

    while total > 0:

        #print(listErrorGrid)
        maxError, indice = MaxOfList(listErrorGrid)

        i = int(indice / 3)  #Indice de la case 3*3
        j = indice % 3

        print(indice)


        while listErrorGrid[indice] >= maxError:   #Tq l'erreur de la case est la plus grande

            print("case :")
            print(listErrorGrid[i])

            while TotalError(listErrorGrid) >= total:  #Tq le changement de la case n'apporte pas d'améliorations

                print(TotalError(listErrorGrid))

                FillGrid(inGrid, grid, i, j)  # Remélange une case

                lignError, columnError = CountError(grid)  # Permet de compter les erreurs
                listErrorGrid = ClassifyError(lignError, columnError)  # Permet de compter les erreurs

            total = TotalError(listErrorGrid)

            #Changer de
            #i = random.randint(0, 2)
            #j = random.randint(0, 2)







    PrintSudoku(grid)


def AroundCase(indice, i, j):

    initialI = int(indice / 3)
    initialJ = indice % 3








def MaxOfList(list):

    max = 0
    indice = 0

    for i in range(9):

        if list[i]>max:
            max = list[i]
            indice = i

    return max, indice

def TotalError(list):

    total = 0

    for i in range(9):

        total += list[i]

    return total



#Compte les erreurs par ligne et colonne

def CountError(grid):

    #Comptage ligne

    listLignError = [0 for x in range(9)]
    listColumnError = [0 for x in range(9)]

    for l in range(9):

        listNB = []

        for c in range(9):

            if not isInList(grid[l][c], listNB):

                if isErrorLign(listNB, grid, l, c):

                    listLignError[l] += 1


    for c in range(9):

        listNB = []

        for l in range(9):

            if not isInList(grid[l][c], listNB):

                if isErrorColumn(listNB, grid, l, c):

                    listColumnError[c] += 1

    return listLignError,listColumnError

#Somme des erreurs par case

def ClassifyError(lignError, columnError):

    listErrorGrid = []

    for i in range(3):

        errorL = 0

        for l in range(i * 3 , i * 3 + 3):

            errorL += lignError[l]

        for j in range(3):

            errorC = 0

            for c in range(j * 3 , j * 3 + 3):

                errorC += columnError[c]

            listErrorGrid.append(errorC + errorL)

    return listErrorGrid

def isInList(var, list):

    for i in list:
        if var == i:
            return True

    return False

def isErrorLign(listNB, grid, l, c):

    for i in range(9):

        if grid[l][i] == grid[l][c] and c != i :      #verif ligne

            listNB.append(grid[l][c])
            return True

    return False

def isErrorColumn(listNB, grid, l, c):

    for i in range(9):

        if grid[i][c] == grid[l][c] and l != i :      #verif ligne

            listNB.append(grid[l][c])
            return True

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

def PrintSudoku(puzzle):
    """Prints the sudoku board"""
    print("+" + "---+" * 9)
    for i, row in enumerate(puzzle):
        print(("|" + " {}   {}   {} |" * 3).format(*[x if x != 0 else " " for x in row]))
        if i % 3 == 2:
            print("+" + "---+" * 9)
        else:
            print("+" + "   +" * 9)