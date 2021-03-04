from tkinter import *
import time
import random
import itertools
from PIL import ImageTk, Image
from winsound import *
import pygame

# Create variables for our canvas height and width
# We can use these later
canvas_height = 600
canvas_width = 600
tk = Tk()
canvas = Canvas(tk, bg="white", width=canvas_width, height=canvas_height)
canvas.pack()

# Sudoku Title
sudoku_text = canvas.create_text(250, 10, text="Sudoku", font=(None, 24, 'bold'), fill="red", anchor=NW)


# Create 9x9 Grid
grid_outline = canvas.create_rectangle(48, 48, 547, 509)
grid_outline2 = canvas.create_rectangle(49, 49, 548, 510)
grid_outline3 = canvas.create_rectangle(50, 50, 549, 511)
line1 = canvas.create_line(50, 205, 550, 205)
line1_2 = canvas.create_line(50, 206, 550, 206)
line1_3 = canvas.create_line(50, 207, 550, 207)
line2 = canvas.create_line(50, 357, 550, 357)
line2_2 = canvas.create_line(50, 358, 550, 358)
line2_3 = canvas.create_line(50, 359, 550, 359)
line3 = canvas.create_line(215, 50, 215, 509)
line3_1 = canvas.create_line(216, 50, 216, 509)
line3_2 = canvas.create_line(217, 50, 217, 509)
line4 = canvas.create_line(381, 50, 381, 509)
line4_2 = canvas.create_line(382, 50, 382, 509)
line4_3 = canvas.create_line(383, 50, 383, 509)

# Function that creates the rest of the row based on one cell
def create_row(x1, y1, x2, y2):
    count = 1
    for i in range(8):
        if count % 3 == 0:
            x1 += 56
            x2 += 56
        else:
            x1 += 55
            x2 += 55
        temp = canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        cell_list.append(temp)
        count += 1

# References for each row
row_1 = canvas.create_rectangle(50, 50, 105, 105, fill="white")
row_2 = canvas.create_rectangle(50, 105, 105, 155, fill="white")
row_3 = canvas.create_rectangle(50, 155, 105, 205, fill="white")
row_4 = canvas.create_rectangle(50, 207, 105, 257, fill="white")
row_5 = canvas.create_rectangle(50, 257, 105, 307, fill="white")
row_6 = canvas.create_rectangle(50, 307, 105, 357, fill="white")
row_7 = canvas.create_rectangle(50, 359, 105, 409, fill="white")
row_8 = canvas.create_rectangle(50, 409, 105, 459, fill="white")
row_9 = canvas.create_rectangle(50, 459, 105, 509, fill="white")

# List of references for each row
row_list = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]

cell_list = []

# Go through the references and call the function create_row 
for row in row_list:
    cell_list.append(row)
    curr_coords = canvas.coords(row)
    create_row(curr_coords[0], curr_coords[1], curr_coords[2], curr_coords[3])

def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 

my_dict = {}
matrix = [[0]*9 for i in range(9)]
# Create a 2D Array to store all of the moves
x = 0
for i in range(9):
    print()
    for j in range(9):
        str_i = str(i)
        str_j = str(j)
        my_dict[cell_list[x]] = str_i + str_j
        x += 1


pygame.mixer.init()
def play_music():
    pygame.mixer.music.set_volume(.1)
    pygame.mixer.music.load("wrong.mp3")
    pygame.mixer.music.play()


global answer_incorrect_label
answer_incorrect_label = canvas.create_text(0, 0, fill="")

def compare_to_answer(index, curr_num):
    int_i = int(index[0])
    int_j = int(index[1])
    for x in my_dict:    
        if curr_num == temp_matrix[int_i][int_j]:
            return True
            break
        else:
            play_music()
            return False
            break

# When you click on a number, it stores that corresponding image to the img_actual variable
def click_event(event):
    global curr_num
    global answer_incorrect_label
    if canvas.find_withtag(CURRENT):  
        curr_coords = canvas.coords(CURRENT)
        assign_number(curr_coords)
        for x in my_dict:
            if canvas.coords(x) == curr_coords:
                if(compare_to_answer(my_dict[x], curr_num)):
                    assign_move(my_dict[x])
                    if curr_num == 1:
                        img_actual = canvas.create_image(canvas.coords(x)[0] + 3, canvas.coords(x)[1], image=img1, anchor=NW)
                    elif curr_num == 2:
                        img_actual = canvas.create_image(canvas.coords(x)[0] + 3, canvas.coords(x)[1], image=img2, anchor=NW)
                    elif curr_num == 3:
                        img_actual = canvas.create_image(canvas.coords(x)[0] + 3, canvas.coords(x)[1], image=img3, anchor=NW)
                    elif curr_num == 4:
                        img_actual = canvas.create_image(canvas.coords(x)[0] + 3, canvas.coords(x)[1], image=img4, anchor=NW)
                    elif curr_num == 5:
                        img_actual = canvas.create_image(canvas.coords(x)[0] + 3, canvas.coords(x)[1], image=img5, anchor=NW)
                    elif curr_num == 6:
                        img_actual = canvas.create_image(canvas.coords(x)[0] + 3, canvas.coords(x)[1], image=img6, anchor=NW)
                    elif curr_num == 7:
                        img_actual = canvas.create_image(canvas.coords(x)[0] + 3, canvas.coords(x)[1], image=img7, anchor=NW)
                    elif curr_num == 8:
                        img_actual = canvas.create_image(canvas.coords(x)[0] + 3, canvas.coords(x)[1], image=img8, anchor=NW)
                    elif curr_num == 9:
                        img_actual = canvas.create_image(canvas.coords(x)[0] + 3, canvas.coords(x)[1], image=img9, anchor=NW)
                    cell_list.remove(x)
                    

canvas.bind_all('<Button-1>', click_event)

img = Image.open("1.png")
img1 = ImageTk.PhotoImage(img)
img_actual = canvas.create_image(63, 525, image=img1, anchor=NW)
img = Image.open("2.png")
img2 = ImageTk.PhotoImage(img)
img_actual = canvas.create_image(118, 525, image=img2, anchor=NW)
img = Image.open("3.png")
img3 = ImageTk.PhotoImage(img)
img_actual = canvas.create_image(168, 525, image=img3, anchor=NW)
img = Image.open("4.png")
img4 = ImageTk.PhotoImage(img)
img_actual = canvas.create_image(220, 525, image=img4, anchor=NW)
img = Image.open("5.png")
img5 = ImageTk.PhotoImage(img)
img_actual = canvas.create_image(270, 525, image=img5, anchor=NW)
img = Image.open("6.png")
img6 = ImageTk.PhotoImage(img)
img_actual = canvas.create_image(320, 525, image=img6, anchor=NW)
img = Image.open("7.png")
img7 = ImageTk.PhotoImage(img)
img_actual = canvas.create_image(372, 525, image=img7, anchor=NW)
img = Image.open("8.png")
img8 = ImageTk.PhotoImage(img)
img_actual = canvas.create_image(422, 525, image=img8, anchor=NW)
img = Image.open("9.png")
img9 = ImageTk.PhotoImage(img)
img_actual = canvas.create_image(472, 525, image=img9, anchor=NW)


global indicator
indicator = canvas.create_rectangle(0, 0, 0, 0, fill="", outline="")

# Create number indicator
def create_num_indicator(coord1, coord2):
    global indicator
    
    canvas.delete(indicator)
    indicator = canvas.create_rectangle(coord1, coord2, coord1+50, coord2+50, outline="red")
        
    
# Checks for which number the user clicked on and stores that number in curr_num 
curr_num = 0
def assign_number(coords):
    global curr_num
    if coords[0] == float(63) and coords[1] == float(525):
        curr_num = 1
        create_num_indicator(63, 525)
    elif coords[0] == float(118) and coords[1] == float(525):
        curr_num = 2
        create_num_indicator(118, 525)
    elif coords[0] == float(168) and coords[1] == float(525):
        curr_num = 3
        create_num_indicator(168, 525)
    elif coords[0] == float(220) and coords[1] == float(525):
        curr_num = 4
        create_num_indicator(220, 525)
    elif coords[0] == float(270) and coords[1] == float(525):
        curr_num = 5
        create_num_indicator(270, 525)
    elif coords[0] == float(320) and coords[1] == float(525):
        curr_num = 6
        create_num_indicator(320, 525)
    elif coords[0] == float(372) and coords[1] == float(525):
        curr_num = 7
        create_num_indicator(372, 525)
    elif coords[0] == float(422) and coords[1] == float(525):
        curr_num = 8
        create_num_indicator(422, 525)
    elif coords[0] == float(472) and coords[1] == float(525):
        curr_num = 9
        create_num_indicator(472, 525)

# Stores the curr_num into the 2d matrix to compare later
def assign_move(index):
    int_i = int(index[0])
    int_j = int(index[1])
    matrix[int_i][int_j] = curr_num

def check_around(i, j):
    pass

def check_row_duplicates(target_num, rand_i, rand_j):
    temp_arr = []
    for i in range(9):
        temp_arr.append(matrix[rand_i][i])
        temp_arr.append(matrix[i][rand_j])

    myset = set(temp_arr)

    myset = myset.union(check_grid(rand_i, rand_j))

    if len(myset) == 10:
        return 0

    while target_num in myset:
        target_num = random.randint(1, 9)
        if target_num not in myset:
            return target_num

    return target_num

def check_grid(i, j):
    global r1,r2,r3,r4,r5,r6,r7,r8,r9
    r1 = matrix[0]
    r2 = matrix[1]
    r3 = matrix[2]
    r4 = matrix[3]
    r5 = matrix[4]
    r6 = matrix[5]
    r7 = matrix[6]
    r8 = matrix[7]
    r9 = matrix[8]

    sec1 = [r1, r2, r3]
    sec2 = [r4, r5, r6]
    sec3 = [r7, r8, r9]

    result = set()

    if i < 2 and j < 2:
        for row in sec1:
            for n in row[:3]:
                result.add(n)
    
    if (i >= 0 and i <= 2) and (j >= 3 and j <= 5):
        for row in sec1:
            for n in row[3:6]:
                result.add(n)

    if (i >= 0 and i <= 2) and (j >= 6 and j <= 8):
        for row in sec1:
            for n in row[6:9]:
                result.add(n)

    if (i >= 3 and i <= 5) and (j >= 0 and j <= 2):
        for row in sec2:
            for n in row[:3]:
                result.add(n)

    if (i >= 3 and i <= 5) and (j >= 3 and j <= 5):
        for row in sec2:
            for n in row[3:6]:
                result.add(n)

    if (i >= 3 and i <= 5) and (j >= 6 and j <= 8):
        for row in sec2:
            for n in row[6:9]:
                result.add(n)

    if (i >= 6 and i <= 8) and (j >= 0 and j <= 2):
        for row in sec3:
            for n in row[:3]:
                result.add(n)

    if (i >= 6 and i <= 8) and (j >= 3 and j <= 5):
        for row in sec3:
            for n in row[3:6]:
                result.add(n)

    if (i >= 6 and i <= 8) and (j >= 6 and j <= 8):
        for row in sec3:
            for n in row[6:9]:
                result.add(n)

    return result
    
def check_for_break(i, j):
    if matrix[i][j] == 0:
        return True

def check_sudoku(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            # check value is an int
            if grid[row][col] < 1 or type(grid[row][col]) is not type(1):
                return False
            # check value is within 1 through n.
            # for example a 2x2 grid should not have the value 8 in it
            elif grid[row][col] > len(grid):
                return False
    # check the rows
    for row in grid:
        if sorted(list(set(row))) != sorted(row):
            return False
    # check the cols
    cols = []
    for col in range(len(grid)):
        for row in grid:
            cols += [row[col]]
        # set will get unique values, its converted to list so you can compare
        # it's sorted so the comparison is done correctly.
        if sorted(list(set(cols))) != sorted(cols):
            return False
        cols = []
    # if you get past all the false checks return True
    return True

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

valid_matrix = False

global temp_matrix
temp_matrix = [[0]*9 for i in range(9)]


# This is how you change the amount of numbers on the board
while not valid_matrix:
    for i in range(30):
        rand_num = random.randint(1, 9)
        rand_i = random.randint(0, 8)
        rand_j = random.randint(0, 8)

        while(check_for_break(rand_i, rand_j)):
            index_str = str(rand_i) + str(rand_j)
            rand_num = check_row_duplicates(rand_num, rand_i, rand_j)
            matrix[rand_i][rand_j] = rand_num


    for i in range(9):
        for j in range(9):
            temp_matrix[i][j] = matrix[i][j]
    solve(temp_matrix)
    print("SOLVED MATRIX", temp_matrix)

    if check_sudoku(temp_matrix):
        break
    else:
        matrix = [[0]*9 for i in range(9)]
        r1.clear()
        r2.clear()
        r3.clear()
        r4.clear()
        r5.clear()
        r6.clear()
        r7.clear()
        r8.clear()
        r9.clear()

def assign_pictures(rand_num, index_str):
    if rand_num == 1:
        temp_img = canvas.create_image(canvas.coords(get_key(index_str))[0] + 3, canvas.coords(get_key(index_str))[1], image=img1, anchor=NW)
    elif rand_num == 2:
        temp_img = canvas.create_image(canvas.coords(get_key(index_str))[0] + 3, canvas.coords(get_key(index_str))[1], image=img2, anchor=NW)
    elif rand_num == 3:
        temp_img = canvas.create_image(canvas.coords(get_key(index_str))[0] + 3, canvas.coords(get_key(index_str))[1], image=img3, anchor=NW)
    elif rand_num == 4:
        temp_img = canvas.create_image(canvas.coords(get_key(index_str))[0] + 3, canvas.coords(get_key(index_str))[1], image=img4, anchor=NW)
    elif rand_num == 5:
        temp_img = canvas.create_image(canvas.coords(get_key(index_str))[0] + 3, canvas.coords(get_key(index_str))[1], image=img5, anchor=NW)
    elif rand_num == 6:
        temp_img = canvas.create_image(canvas.coords(get_key(index_str))[0] + 3, canvas.coords(get_key(index_str))[1], image=img6, anchor=NW)
    elif rand_num == 7:
        temp_img = canvas.create_image(canvas.coords(get_key(index_str))[0] + 3, canvas.coords(get_key(index_str))[1], image=img7, anchor=NW)
    elif rand_num == 8:
        temp_img = canvas.create_image(canvas.coords(get_key(index_str))[0] + 3, canvas.coords(get_key(index_str))[1], image=img8, anchor=NW)
    elif rand_num == 9:
        temp_img = canvas.create_image(canvas.coords(get_key(index_str))[0] + 3, canvas.coords(get_key(index_str))[1], image=img9, anchor=NW)

def get_i_j(i, j):
    index_str = str(i) + str(j)
    return index_str

for i in range(9):
        for j in range(9):
            assign_pictures(matrix[i][j], get_i_j(i,j))

mainloop()
def game_loop():
    while True:
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

# game_loop()