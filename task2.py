#!python3
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="Client Database")
button1 = tk.Button(window, text="Search by Name")
entry1 = tk.Entry(window, width=15)
#row1
label3 = tk.Label(window, text="Name")
label4 = tk.Label(window, text="Type")
label5 = tk.Label(window, text="Breed")
label6 = tk.Label(window, text="Owner")
label7 = tk.Label(window, text="Birthdate")
#row2
entry2 = tk.Entry(window, width=10)
entry3 = tk.Entry(window, width=10)
entry4 = tk.Entry(window, width=10)
entry5 = tk.Entry(window, width=10)
entry6 = tk.Entry(window, width=10)
#row3
button2 = tk.Button(window, text="< Previous")
button3 = tk.Button(window, text="Save Entry")
button4 = tk.Button(window, text="Next >")

label1.grid(row=1, column=1)
label2.grid(row=1, column=3)
button1.grid(row=1, column=4)
entry1.grid(row=1, column=5)
label3.grid(row=2, column=1)
label4.grid(row=2, column=2)
label5.grid(row=2, column=3)
label6.grid(row=2, column=4)
label7.grid(row=2, column=5)
entry2.grid(row=3, column=1)
entry3.grid(row=3, column=2)
entry4.grid(row=3, column=3)
entry5.grid(row=3, column=4)
entry6.grid(row=3, column=5)
button2.grid(row=4,column=1)
button3.grid(row=4,column=3)
button4.grid(row=4,column=5)

window.mainloop()