from tkinter import *
import time
import os
import random
from PIL import Image, ImageTk

# Create variables for our canvas height and width
# We can use these later
canvas_height = 900
canvas_width = 1000
tk = Tk()
canvas = Canvas(tk, bg="white", width=canvas_width, height=canvas_height)
canvas.pack()

# Background canvas details
background = canvas.create_rectangle(0, 0, 1005, 800, fill="CadetBlue3", outline="white")

global tkpi
bird_img = Image.open("bird.png")
rotated = bird_img.rotate(0)
tkpi = ImageTk.PhotoImage(rotated)

bg_img = Image.open("bg.png")
rotated2 = bg_img.rotate(0)
tkpi2 = ImageTk.PhotoImage(rotated2)

bird_actual = canvas.create_image(144, 155, image=tkpi, anchor=NW)
create_bg_img = canvas.create_image(0, 0, image=tkpi2, anchor=NW)

# All shapes that make up the bird
bird = canvas.create_oval(150, 160, 200, 200, fill="")
bird_wing = canvas.create_oval(155, 170, 175, 185, fill="")
bird_eye = canvas.create_oval(180, 160, 200, 175, fill="")
bird_pupil = canvas.create_oval(190, 165, 195, 170, fill="")
bird_top_lip = canvas.create_oval(184, 185, 204, 192, fill="")
bird_bottom_lip = canvas.create_oval(184, 190, 204, 197, fill="")
canvas.itemconfig(bird, outline="")
canvas.itemconfig(bird_wing, outline="")
canvas.itemconfig(bird_eye, outline="")
canvas.itemconfig(bird_pupil, outline="")
canvas.itemconfig(bird_top_lip, outline="")
canvas.itemconfig(bird_bottom_lip, outline="")

bird_parts = [bird, bird_wing, bird_eye, bird_pupil, bird_top_lip, bird_bottom_lip]

# Our Pipes
pipe_1_top = canvas.create_rectangle(500, 0, 550, 300, fill="green")
pipe_1_bot = canvas.create_rectangle(500, 450, 550, 800, fill="green")

pipe_2_top = canvas.create_rectangle(800, 0, 750, 500, fill="green")
pipe_2_bot = canvas.create_rectangle(800, 650, 750, 800, fill="green")

pipe_3_top = canvas.create_rectangle(1100, 0, 1050, 400, fill="green")
pipe_3_bot = canvas.create_rectangle(1100, 550, 1050, 800, fill="green")

pipe_4_top = canvas.create_rectangle(1400, 0, 1350, 200, fill="green")
pipe_4_bot = canvas.create_rectangle(1400, 350, 1350, 800, fill="green")

pipe_5_top = canvas.create_rectangle(1700, 0, 1650, 300, fill="green")
pipe_5_bot = canvas.create_rectangle(1700, 450, 1650, 800, fill="green")

pipe_heights = [300, 450, 350, 500, 400, 550, 450, 600, 500, 650]

pipes = [pipe_1_top, pipe_1_bot, pipe_2_top, pipe_2_bot, pipe_3_top, pipe_3_bot, pipe_4_top, pipe_4_bot, pipe_5_top, pipe_5_bot]

# The ground for the game
top_ground = canvas.create_rectangle(-5, 800, 1005, 820, fill="yellow green")
bottom_ground = canvas.create_rectangle(-5, 820, 1005, 910, fill="khaki2")


def generate_top_rim(pipe):
    pipe_pos = canvas.coords(pipe)
    top_rim = canvas.create_rectangle(pipe_pos[0]-10, pipe_pos[3] - 20, pipe_pos[2]+10, pipe_pos[3], fill="green")
    return top_rim

def generate_bottom_rim(pipe):
    pipe_pos = canvas.coords(pipe)
    bot_rim = canvas.create_rectangle(pipe_pos[0]-10, pipe_pos[1], pipe_pos[0]+60, pipe_pos[1]+20, fill="green")
    return bot_rim

# Generate rims for existing pipes
pipe_1_top_rim = generate_top_rim(pipe_1_top)
pipe_2_top_rim = generate_top_rim(pipe_2_top)
pipe_3_top_rim = generate_top_rim(pipe_3_top)
pipe_4_top_rim = generate_top_rim(pipe_4_top)
pipe_5_top_rim = generate_top_rim(pipe_5_top)

pipe_1_bot_rim = generate_bottom_rim(pipe_1_bot)
pipe_2_bot_rim = generate_bottom_rim(pipe_2_bot)
pipe_3_bot_rim = generate_bottom_rim(pipe_3_bot)
pipe_4_bot_rim = generate_bottom_rim(pipe_4_bot)
pipe_5_bot_rim = generate_bottom_rim(pipe_5_bot)

pipe_rims = [pipe_1_top_rim, pipe_2_top_rim, pipe_3_top_rim, pipe_4_top_rim, pipe_5_top_rim, pipe_1_bot_rim, pipe_2_bot_rim, pipe_3_bot_rim, pipe_4_bot_rim, pipe_5_bot_rim]

def move_pipes():
    for pipe in pipes:
        canvas.move(pipe, -1, 0)

    for pipe_rim in pipe_rims:
        canvas.move(pipe_rim, -1, 0)

def generate_pipe():
    rand_num = random.randint(0,4)*2
    print(rand_num)
    top_pipe = canvas.create_rectangle(1400, 0, 1350, pipe_heights[rand_num], fill="green")
    bot_pipe = canvas.create_rectangle(1400, pipe_heights[rand_num+1], 1350, 800, fill="green")
    pipes.append(top_pipe)
    pipes.append(bot_pipe)
    pipe_rims.append(generate_top_rim(top_pipe))
    pipe_rims.append(generate_bottom_rim(bot_pipe))

def move_square(event):
    global tkpi
    global bird_actual
    global temp_bird_pos
    if event.keysym == 'space' and stop_bird != True:
        temp_bird_pos = bird_pos
        print(temp_bird_pos)
        rotated = bird_img.rotate(45)
        tkpi = ImageTk.PhotoImage(rotated)
        bird_actual = canvas.create_image(bird_pos[0]-6, bird_pos[1]-5, image=tkpi, anchor=NW)

        canvas.move(bird_actual, 0, -60)
        canvas.move(bird, 0, -60)
        canvas.move(bird_wing, 0, -60)
        canvas.move(bird_eye, 0, -60)
        canvas.move(bird_pupil, 0, -60)
        canvas.move(bird_top_lip, 0, -60)
        canvas.move(bird_bottom_lip, 0, -60)

canvas.bind_all('<space>', move_square)

def move_bird():
    global bird_actual
    canvas.move(bird_actual, 0, 1)
    canvas.move(bird, 0, 1)
    canvas.move(bird_wing, 0, 1)
    canvas.move(bird_eye, 0, 1)
    canvas.move(bird_pupil, 0, 1)
    canvas.move(bird_top_lip, 0, 1)
    canvas.move(bird_bottom_lip, 0, 1)

def bird_drop():
    canvas.move(bird_actual, 0, 1)
    canvas.move(bird, 0, 1)
    canvas.move(bird_wing, 0, 1)
    canvas.move(bird_eye, 0, 1)
    canvas.move(bird_pupil, 0, 1)
    canvas.move(bird_top_lip, 0, 1)
    canvas.move(bird_bottom_lip, 0, 1)

def did_collide(shape1, shape2):
    pos1 = canvas.coords(shape1)
    pos2 = canvas.coords(shape2)
    if pos1[2] >= pos2[0] and pos1[0] <= pos2[2]:
        if pos1[3] >= pos2[1] and pos1[1] <= pos2[3]:
            return True
    return False

def delete_on_collision(shape1, shape2):
    global stop_bird
    if did_collide(shape1, shape2):
        stop_bird = True

# mainloop()

# Score Text on Canvas
score_text = canvas.create_text(500, 200, text="0")
canvas.itemconfig(score_text, font=("Courier", 44))
score = 0

stop_bird = False
temp_bird_pos = [150, 160, 200, 200]
def game_loop():
    global stop_bird
    global score
    global tkpi
    global bird_img
    global bird_pos
    global bird_actual
    seconds = 0
    while True:
        bird_pos = canvas.coords(bird)

        if abs(temp_bird_pos[1] - bird_pos[1]) == 10:
            rotated = bird_img.rotate(-25)
            tkpi = ImageTk.PhotoImage(rotated)
            bird_actual = canvas.create_image(bird_pos[0] - 6, bird_pos[1] - 5, image=tkpi, anchor=NW)

        if stop_bird != True:
            move_bird()
            move_pipes()
        elif bird_pos[1] < canvas_height - 140:
            bird_drop()

        for pipe in pipes:
            delete_on_collision(bird, pipe)

        for pipe in pipes:
            pipe_pos = canvas.coords(pipe)
            if pipe_pos[0] < -50 and pipe_pos[1] < 299:
                pipes.remove(pipe)
                generate_pipe()

        # Remove excess pipe rims
        # for pipe_rim in pipe_rims:
        #     pipe_pos = canvas.coords(pipe_rim)
        #     if pipe_pos[0] < -50:
        #         pipe_rims.remove(pipe_rim)

        # Keeps track of score
        for pipe in pipes:
            pipe_pos = canvas.coords(pipe)
            if pipe_pos[0] < 150 and pipe_pos[0] >= 148.8:
                score = score + .5
                canvas.itemconfig(score_text, text=int(score))

        canvas.tag_raise(score_text)

        tk.update_idletasks()
        tk.update()
        tk.after(3)

game_loop()