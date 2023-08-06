from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")

hello = tk.Label(text="Welcome to Spelling Bee's Spelling Game")
hello.pack()
button = tk.Button(text="")
button.pack()
 
tk.mainloop()