from tkinter import *
import time
import random
import numpy as np
from PIL import ImageTk, Image

# Create variables for our canvas height and width
# We can use these later
canvas_height = 500
canvas_width = 500
tk = Tk()
canvas = Canvas(tk, bg="white", width=canvas_width, height=canvas_height)
canvas.pack()

# First Row
cell1 = canvas.create_rectangle(50, 50, 183, 183, fill="white", outline="")
cell2 = canvas.create_rectangle(183, 50, 316, 183, fill="white", outline="")
cell3 = canvas.create_rectangle(316, 50, 450, 183, fill="white", outline="")

# Second Row
cell4 = canvas.create_rectangle(50, 183, 183, 316, fill="white", outline="")
cell5 = canvas.create_rectangle(183, 183, 316, 316, fill="white", outline="")
cell6 = canvas.create_rectangle(316, 183, 450, 316, fill="white", outline="")

# Third Row
cell7 = canvas.create_rectangle(50, 316, 183, 450, fill="white", outline="")
cell8 = canvas.create_rectangle(183, 316, 316, 450, fill="white", outline="")
cell9 = canvas.create_rectangle(316, 316, 450, 450, fill="white", outline="")

# Store all cells in a list
cell_list = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]

# 3x3 Grid
line1 = canvas.create_line(183, 50, 183, 450)
line1_2 = canvas.create_line(182, 50, 182, 450)
line1_3 = canvas.create_line(184, 50, 184, 450)

line2 = canvas.create_line(316, 50, 316, 450)
line2_2 = canvas.create_line(315, 50, 315, 450)
line2_3 = canvas.create_line(317, 50, 317, 450)

line3 = canvas.create_line(50, 183, 450, 183)
line3_2 = canvas.create_line(50, 182, 450, 182)
line3_3 = canvas.create_line(50, 184, 450, 184)

line4 = canvas.create_line(50, 316, 450, 316)
line4_2 = canvas.create_line(50, 315, 450, 315)
line4_3 = canvas.create_line(50, 317, 450, 317)

my_dict = {}
matrix = [[0]*3 for i in range(3)]
# Create a 2D Array to store all of the moves
x = 0
for i in range(3):
    print()
    for j in range(3):
        str_i = str(i)
        str_j = str(j)
        my_dict[cell_list[x]] = str_i + str_j
        x += 1

print(my_dict)

global game_over
game_over = False

# [1 is X] and [2 is O]
currMove = 1

def click_event(event):
    global currMove
    if canvas.find_withtag(CURRENT):
        curr_coords = canvas.coords(CURRENT)
        for x in my_dict:
            if canvas.coords(x) == curr_coords and not game_over:
                #print(my_dict[x])
                
                assign_move(my_dict[x])
                if currMove == 1:
                    img_actual = canvas.create_image(canvas.coords(x)[0] + 7, canvas.coords(x)[1] + 7, image=img1, anchor=NW)
                    currMove = 2
                else: 
                    img_actual = canvas.create_image(canvas.coords(x)[0] + 7, canvas.coords(x)[1] + 7, image=img2, anchor=NW)
                    currMove = 1
                cell_list.remove(x)
                print(currMove)

canvas.bind_all('<Button-1>', click_event)

def assign_move(index):
    int_i = int(index[0])
    int_j = int(index[1])
    matrix[int_i][int_j] = currMove
    print(matrix)
    

def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def checkWin(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)

img = Image.open("X.png")
img1 = ImageTk.PhotoImage(img)

img = Image.open("O.png")
img2 = ImageTk.PhotoImage(img)


# mainloop()
def game_loop():
    global game_over
    while True:
        if checkWin(matrix) == 1:
            win_text = canvas.create_text(130, 10, font=(None, 24), fill="red", text="Player 1 has won!", anchor=NW)
            game_over = True

        
        if checkWin(matrix) == 2:
            win_text = canvas.create_text(130, 10, font=(None, 24), fill="red", text="Player 2 has won!", anchor=NW)
            game_over = True
        
        count = 0
        for i in range(3):
            for j in range(3):
                if matrix[i][j] != 0:
                    count += 1

        if count == 9 and checkWin(matrix) != 1 and checkWin(matrix) != 2:
            win_text = canvas.create_text(210, 10, font=(None, 24), fill="red", text="Draw!", anchor=NW)
            game_over = True

        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

game_loop()