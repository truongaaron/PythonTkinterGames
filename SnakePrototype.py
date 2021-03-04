from tkinter import *
import time
import random

# Create variables for our canvas height and width
# We can use these later
canvas_height = 500
canvas_width = 500
tk = Tk()
canvas = Canvas(tk, bg="white", width=canvas_width, height=canvas_height)
canvas.pack()

# The inital Snake position (center of the canvas)
snake = canvas.create_rectangle(240, 240, 260, 260, fill="black")

# This coordinates array keeps track of all of the possible coordinates of the apples so we could randomize it on the canvas later
apple_coords_arr = []


# This function stores the coordinates for every possible apple on the canvas board (24x24)
def store_apple_coords():
    x1 = 5
    y1 = 5
    x2 = 15
    y2 = 15

    x1_ = 5
    y1_ = 5
    x2_ = 15
    y2_ = 15
    apple_coords_arr.append(x1)
    apple_coords_arr.append(y1)
    apple_coords_arr.append(x2)
    apple_coords_arr.append(y2)
    for col in range(24):
        for row in range(24):
            x1 = x1 + 20
            x2 = x2 + 20
            apple_coords_arr.append(x1)
            apple_coords_arr.append(y1)
            apple_coords_arr.append(x2)
            apple_coords_arr.append(y2)
        x1 = x1_
        x2 = x2_

        y1 = y1_ + 20
        y1_ = y1_ + 20
        y2 = y2_ + 20
        y2_ = y2_ + 20


# Call the function to generate apples in the array and append all coordinates to apple_coords_arr
store_apple_coords()

# This random number is generated and multiplied by 4 because there are total of 2,504 coordinates
random_num = random.randint(0, 576) * 4

# This is the initial apple that is spawned on the canvas (it is destroyed and replaced when snake eats it)
apple = canvas.create_oval(apple_coords_arr[random_num], apple_coords_arr[random_num + 1],
                           apple_coords_arr[random_num + 2], apple_coords_arr[random_num + 3], fill="red",
                           outline="white")

# Stores every new rectangle object that is created to be able to update body positions
snake_body_list = [snake]


# These are the general bounds for the canvas, the snake can't pass these bounds or the game will crash.
def snake_bounds():
    global stop_snake
    # canvas.move(snake, snake_x, snake_y)
    pos = canvas.coords(snake)
    # pos = [100.0, 100.0, 150.0, 150.0]
    # Check if x1 is out of bounds
    if pos[0] < 0:
        print("You went out of bounds! You have lost the game!")
        stop_snake = True
        snake_body_list.clear()
        create_end_text()
    # Check if x2 is out of bounds
    if pos[2] > canvas_width:
        print("You went out of bounds! You have lost the game!")
        stop_snake = True
        snake_body_list.clear()
        create_end_text()
    # Check if y1 is out of bounds
    if pos[1] < 0:
        print("You went out of bounds! You have lost the game!")
        stop_snake = True
        snake_body_list.clear()
        create_end_text()
    # Check if y2 is out of bounds
    if pos[3] > canvas_height:
        print("You went out of bounds! You have lost the game!")
        stop_snake = True
        snake_body_list.clear()
        create_end_text()


# If snake body goes out of bounds
def create_end_text():
    canvas.create_text(250, 100, text="You went out of bounds! You have lost the game!")
    canvas.create_text(250, 120, text="Your final score is " + str(score))


# If snake body eats itself
def create_end_text_2():
    canvas.create_text(250, 100, text="You tried to eat yourself! You have lost the game!")
    canvas.create_text(250, 120, text="Your final score is " + str(score))


# Checks if one shape collides with the other shape
def did_collide(shape1, shape2):
    pos1 = canvas.coords(shape1)
    pos2 = canvas.coords(shape2)
    if pos1[2] > pos2[0] and pos1[0] < pos2[2]:
        if pos1[3] > pos2[1] and pos1[1] < pos2[3]:
            return True
    return False


# Creates apple and snake grows size whenever the body collides with the apple
def create_apple_and_body_on_collision(shape1, shape2):
    if did_collide(shape1, shape2):
        global apple
        global score
        score = score + 1
        canvas.itemconfig(score_text, text=score)
        random_num = random.randint(0, 576) * 4
        canvas.delete(apple)
        apple = canvas.create_oval(apple_coords_arr[random_num], apple_coords_arr[random_num + 1],
                                   apple_coords_arr[random_num + 2], apple_coords_arr[random_num + 3], fill="red",
                                   outline="white")
        make_new_body()


# General function for deleting a shape when one touches the other, but this prompts that you lose the game
def delete_on_collision(shape1, shape2):
    global stop_snake
    if did_collide(shape1, shape2):
        stop_snake = True
        snake_body_list.clear()
        create_end_text_2()


# Array that keeps track of all of the initial snake body coordinates
body_pos = []


def make_new_body():
    snake_body = canvas.create_rectangle(body_pos[len(body_pos) - 1][0], body_pos[len(body_pos) - 1][1],
                                         body_pos[len(body_pos) - 1][2], body_pos[len(body_pos) - 1][3], fill="black")
    snake_body_list.append(snake_body)


# mainloop()

# All basic functions for the snake to move (used for the game loop)
def move_up(shape):
    for shape in snake_body_list:
        canvas.move(shape, 0, -20)


def move_down(shape):
    for shape in snake_body_list:
        canvas.move(shape, 0, 20)


def move_left(shape):
    for shape in snake_body_list:
        canvas.move(shape, -20, 0)


def move_right(shape):
    for shape in snake_body_list:
        canvas.move(shape, 20, 0)


# This function is bound to the keys Up, Left, Down, and Right, used to flag for the game loop animations
def move_square(event):
    global up_pressed
    global down_pressed
    global left_pressed
    global right_pressed

    if event.keysym == 'Up' and down_pressed != True:
        snake_bounds()
        up_pressed = True
        down_pressed = False
        left_pressed = False
        right_pressed = False
    elif event.keysym == 'Down' and up_pressed != True:
        snake_bounds()
        up_pressed = False
        down_pressed = True
        left_pressed = False
        right_pressed = False
    elif event.keysym == 'Left' and right_pressed != True:
        snake_bounds()
        up_pressed = False
        down_pressed = False
        left_pressed = True
        right_pressed = False
    elif event.keysym == 'Right' and left_pressed != True:
        snake_bounds()
        up_pressed = False
        down_pressed = False
        left_pressed = False
        right_pressed = True


# Initialize the values of the keys pressed
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

canvas.bind_all('<Up>', move_square)
canvas.bind_all('<Down>', move_square)
canvas.bind_all('<Left>', move_square)
canvas.bind_all('<Right>', move_square)

# Score Text on Canvas
score_text = canvas.create_text(250, 50, text="0", fill="red")
canvas.itemconfig(score_text, font=("Courier", 36))
score = 0

stop_snake = False


# The game loop allows for all of the animations to happen like the snake moving and the snake body catching up to itself
def game_loop():
    global stop_snake
    while True:
        if not stop_snake:
            if up_pressed:
                move_up(snake)
            elif down_pressed:
                move_down(snake)
            elif left_pressed:
                move_left(snake)
            elif right_pressed:
                move_right(snake)

        # This is where the snake body is constantly being updated
        for i in range(1, len(snake_body_list)):
            delete_on_collision(snake, snake_body_list[i])
            if not stop_snake:
                canvas.coords(snake_body_list[i], body_pos[len(body_pos) - i][0], body_pos[len(body_pos) - i][1],
                              body_pos[len(body_pos) - i][2], body_pos[len(body_pos) - i][3])

        canvas.tag_raise(score_text)

        create_apple_and_body_on_collision(snake, apple)
        snake_bounds()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.15)

        # This is where we update the snake head's every move so the body has a reference point
        body_pos.append(canvas.coords(snake))


game_loop()
