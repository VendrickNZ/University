from tkinter import *
from tkinter.ttk import * 

window = Tk()

sentence = "Wow, I love tkinter!!!!!!! I also need to write more so that there's enough for the scroll bars \n\n\n\n\n\n\n\n\n\n\nto do stuff!! woo"

h = Scrollbar(window, orient='horizontal')
h.pack(side = BOTTOM, fill = X)

v = Scrollbar(window, orient='vertical')
v.pack(side = RIGHT, fill = Y)

t = Text(window, height=10, width=24, wrap=NONE, xscrollcommand=h.set, yscrollcommand=v.set)
t.insert(INSERT, sentence)
t.pack(expand= 1, fill= BOTH)

h.config(command=t.xview) #for horizontal scrollbar
v.config(command=t.yview) #for vertical scrollbar

window.mainloop()