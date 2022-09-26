from tkinter import *
from tkinter.ttk import *
import random
import time
import csv

name = "Jakib"
start = time.time()
distances = [64, 128, 256, 512]
random.shuffle(distances)
widths = [8, 16, 32]
random.shuffle(widths)
i = 0
distance_i = 0
repetitions = 0
more_reps = 0
total_span = widths[i] + distances[distance_i]
margin = (800 - total_span) / 2
left_rec_colour = "green"


master = Tk()
c = Canvas(master, width=800, height=600)
c.pack()


bottom_left_rec, top_left_rec = margin, margin + widths[i]
bottom_right_rec, top_right_rec = ((margin) + total_span) - widths[i], margin + widths[i] + distances[distance_i]
left_rectangle = c.create_rectangle(bottom_left_rec, 0, top_left_rec, 600, fill="green")
right_rectangle = c.create_rectangle(bottom_right_rec, 0, top_right_rec, 600, fill="blue")


def left_rec_action(arg):
    global i
    global distance_i
    global left_rec_colour
    global repetitions
    if left_rec_colour == "blue":
        return
    c.itemconfig(left_rectangle, fill="blue")
    c.itemconfig(right_rectangle, fill="green")
    left_rec_colour = "blue"
    return

def right_rec_action(arg):
    global i
    global distance_i
    global left_rec_colour
    global repetitions
    global more_reps
    repetitions += 1
    selection_time = (time.time() - start) * 1000

    log = open("fitts_law_experiment_log.txt", "a", newline='')
    log.write(f"{name} {distances[distance_i]} {widths[i]} {repetitions} {selection_time:.1f}\n")
    if left_rec_colour == "blue":
        if i == 2:
            random.shuffle(widths)
            random.shuffle(distances)
            if distance_i == 3:
                c.quit()
                return
            distance_i += 1
            i = 0
            c.itemconfig(right_rectangle, fill="blue")
            c.itemconfig(left_rectangle, fill="green")
            left_rec_colour = "green"
            update_rectangles()
            return
        c.itemconfig(right_rectangle, fill="blue")
        c.itemconfig(left_rectangle, fill="green")
        left_rec_colour = "green"
        if more_reps > 0:
            i += 1
            more_reps = 0
        else:
            more_reps += 1
        update_rectangles()
        return
    return

def update_rectangles():
    global start
    total_span = widths[i] + distances[distance_i]
    margin = (800 - total_span) / 2
    bottom_left_rec, top_left_rec = margin, margin + widths[i]
    bottom_right_rec, top_right_rec = ((margin) + total_span) - widths[i], margin + widths[i] + distances[distance_i]
    c.coords(left_rectangle, bottom_left_rec, 0, top_left_rec, 600)
    c.coords(right_rectangle, bottom_right_rec, 0, top_right_rec, 600)
    start = time.time()

c.tag_bind(left_rectangle, "<ButtonPress-1>", left_rec_action)
c.tag_bind(right_rectangle, "<ButtonPress-1>", right_rec_action)

f = open('fitts_law_experiment_log.txt', 'a')
f.truncate(0)

master.mainloop()
