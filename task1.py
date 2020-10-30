#!python3
import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("tk")

entry1 = tk.Entry(window, width = 10)
entry2 = tk.Entry(window, width = 10)
entry3 = tk.Entry(window, width = 20)
label = tk.Label(window, text = "x")
button = tk.Button(window, text = "=")

entry1.grid(row = 1, column = 1)
label.grid(row = 1, column = 2)
entry2.grid(row = 1, column = 3)
button.grid(row = 1, column = 4)
entry3.grid(row = 1, column = 5)

window.mainloop()