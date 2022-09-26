from tkinter import *
from tkinter import ttk

def clear_data(data):
    return data.set('')

def append(user_input, letter):
    return user_input.set(user_input.get() + (letter))

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
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
clear_button = ttk.Button(frame_right, text="Clear", command=lambda: clear_data(user_input))

input.pack(side="left", padx=(25, 175), pady=5, anchor=W)
clear_button.pack(side="right", padx=20, pady=5, anchor=E)

i, j = 0, 0
for _ in range(26):
    if i == 0:
            button = ttk.Button(frame_bottom_row1, text=board[i][j], width=3, command=lambda x=board[i][j]: append(user_input, x))
            button.grid(row=i, column=j,padx=1,pady=1)
    if i == 1:
            button = ttk.Button(frame_bottom_row2, text=board[i][j], width=3, command=lambda x=board[i][j]: append(user_input, x))
            button.grid(row=i, column=j,padx=1,pady=1)
    if i == 2:
            button = ttk.Button(frame_bottom_row3, text=board[i][j], width=3, command=lambda x=board[i][j]: append(user_input, x))
            button.grid(row=i, column=j,padx=1,pady=1)
    j+=1
    if j >= len(board[i]):
        i+=1
        j=0
    
window.mainloop()