from tkinter import *
from tkinter.ttk import * 
master = Tk()
c = Canvas(master, width=200, height=200)
c.pack()
c.create_rectangle(50, 25, 150, 75, fill="blue")
master.mainloop()