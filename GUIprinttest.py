from tkinter import *
import tkinter as tk
def printGUI():
    hello.destroy()
    button.destroy()
    label = Label(text="Hello")
    label.pack()
window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")

hello = tk.Label(text="Welcome to the Spelling Bee Spelling Game")
hello.pack()
button = tk.Button(text="Print", command=printGUI)
button.pack()
 
tk.mainloop()