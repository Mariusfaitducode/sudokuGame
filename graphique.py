from tkinter import *
from graph_fonctions import *


example_board = [
        [0, 6, 5, 0, 0, 0, 4, 8, 0],
        [0, 7, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],

        [7, 0, 0, 0, 2, 0, 0, 0, 5],
        [0, 4, 0, 0, 5, 0, 0, 9, 0],
        [9, 0, 0, 4, 0, 1, 0, 0, 6],

        [0, 0, 0, 1, 0, 5, 0, 0, 0],
        [0, 0, 2, 7, 0, 3, 8, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0]
    ]

window = Tk()
window.title("Sudoku Game")
window.geometry("1080x720")

# window.config(background='gray')

MIN_SIZE = 2 * TAB_GAP + COTE_TAB
window.minsize(MIN_SIZE, MIN_SIZE)

cnv = Canvas(window, width=COTE_TAB, height=COTE_TAB, background='light gray')

cnv.pack()
cnv.place(x=TAB_GAP, y=TAB_GAP)

draw_grid(cnv)

init_grid(cnv, example_board)

but = Button(window, text="Résoudre", font='Helvetica 15 bold',
             background='light gray', command=(lambda: resolver_button(cnv, example_board)))

but.place(x=2 * TAB_GAP + COTE_TAB, y=TAB_GAP + 3 * COTE_CASE)

# but.pack()


window.mainloop()
