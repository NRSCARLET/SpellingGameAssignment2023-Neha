from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title("Spelling Bee's Spelling Game!")
window.geometry("300x300")

hello = tk.Label(text="Welcome to Spelling Bee's Spelling Game!")
hello.pack()
b1 = tk.Button(text="Register (new user)", fg = '#DA70D6', font = 'verdana 9 bold')
b1.pack()
b2 = tk.Button(text="Login (old user)", fg = '#DA70D6', font = 'helvetica, 9 bold')
b2.pack()
tk.mainloop()