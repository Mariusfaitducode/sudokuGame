# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from ResolverPack.Resolver import *




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #EnterGrid()
    Matrix = [[0 for x in range(9)] for y in range(9)]

    test = [
        [4, 8, 0, 0, 1, 0, 0, 7, 2],
        [0, 9, 0, 0, 0, 0, 0, 4, 0],
        [3, 6, 0, 0, 0, 0, 0, 1, 8],

        [0, 2, 0, 0, 0, 0, 0, 5, 0],
        [6, 0, 0, 4, 0, 9, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 7, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 3, 0, 8, 0, 0, 0],
        [0, 0, 0, 5, 9, 6, 0, 0, 0]
    ]

    test2 = [
        [4, 8, 0, 0, 1, 0, 0, 7, 2],
        [0, 9, 0, 0, 0, 0, 0, 4, 0],
        [3, 6, 0, 0, 0, 0, 0, 1, 8],

        [0, 2, 0, 0, 0, 0, 0, 5, 0],
        [6, 0, 0, 4, 0, 9, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 7, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 3, 0, 8, 0, 0, 0],
        [0, 0, 0, 5, 9, 6, 0, 0, 0]
    ]

    count = 0

    PrintSudoku(test)

    Solver(test)

    print("finish it")

    PrintSudoku(test)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
