import time
import random
import string
from tkinter import *
from tkinter import ttk
import csv

start = time.time()
static_layout = False
target_letters = random.choices(string.ascii_lowercase, k=6)
n_target_letters = 6
curr_block = 1
curr_letter = 0
name = "jakib"
layout = "dynamic"
if static_layout:
    layout = "static"


board_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
board = list('qwertyuiopasdfghjklzxcvbnm')
random.shuffle(board)

window = Tk()
frame_top = ttk.Frame(window)
frame_top.pack(side="top", padx=5,pady=5)
frame_left = ttk.Frame(frame_top)
frame_left.pack(side="left")
frame_right = ttk.Frame(frame_top)
frame_right.pack(side="right")

frame_bottom = ttk.Frame(window, borderwidth=2, relief=RIDGE)
frame_bottom.pack(side="bottom", padx=5,pady=5)

frame_bottom_row1 = ttk.Frame(frame_bottom)
frame_bottom_row1.pack(side=TOP)
frame_bottom_row2 = ttk.Frame(frame_bottom)
frame_bottom_row2.pack()
frame_bottom_row3 = ttk.Frame(frame_bottom)
frame_bottom_row3.pack(side=BOTTOM)


user_input = StringVar()
input = ttk.Label(frame_left, textvariable=user_input, anchor=W, justify=LEFT)
user_input.set(target_letters[0])
input.pack(padx=5, pady=5)

def append(user_input, letter):
    global curr_letter
    global curr_block
    global board
    total_time = (time.time() - start) * 1000

    if layout == "dynamic":
        log = open("experiment_dynamic_log.txt", "a", newline='')
    else:
        log = open("experiment_static_log.txt", "a", newline='')
    log.write(name + " " + layout + " " + letter + " " +  str(curr_block) + "{:.1f}\n".format(total_time))
    if curr_block == 6:
        return user_input.set("FINISHED!!")
    if static_layout == False:
        random.shuffle(board)
        board_maker()
    if curr_letter == n_target_letters - 1:
        curr_letter = 0
        random.shuffle(target_letters)
        curr_block += 1
        return user_input.set(target_letters[curr_letter])
    if letter == target_letters[curr_letter]:
        curr_letter += 1
        return user_input.set(target_letters[curr_letter])
    return

def board_maker():
    i, j, = 0, 0
    for index in range(26):
        if i == 0:
                frame = Frame(frame_bottom_row1, height=64, width=64)
        if i == 1:
                frame = Frame(frame_bottom_row2, height=64, width=64)
        if i == 2:
                frame = Frame(frame_bottom_row3, height=64, width=64)
        frame.pack_propagate(0)
        frame.grid(row=i, column=j)
        button = ttk.Button(frame, text=board[index], width=3, command=lambda x=board[index]: append(user_input, x))
        button.pack(fill=BOTH, expand=1)
        j+=1
        if j >= len(board_rows[i]):
            i+=1
            j=0

if layout == "dynamic":
    f = open('experiment_dynamic_log.txt', 'r+')
    f.truncate(0)
else:
    f = open('experiment_static_log.txt', 'r+') # hard coding ):
    f.truncate(0)

board_maker()
window.mainloop()