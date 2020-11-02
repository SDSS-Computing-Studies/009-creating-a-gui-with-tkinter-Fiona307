#!python3
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Example")
window.geometry("256x131")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label1.place(x=90, y=0)

label2 = tk.Label(window, text="Pochacco!")
label2.place(x=153, y=50)

label3 = tk.Label(window, text="A cuddly little puppy! this is from the same\ncreaters who brought you Keropi and Kero Kero", bg="#A3FFFF")
label3.place(x=0, y=95)

window.mainloop()

