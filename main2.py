


from ResolverPack.Resolver3 import *



# Press the green button in the gutter to run the script.
if __name__ == '__main__':



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

    Solver3(test)

    PrintSudoku(test)







