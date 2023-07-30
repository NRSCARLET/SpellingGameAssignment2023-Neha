import tkinter as tk

window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")

hello = tk.Label(text="Welcome to spelling game")
hello.pack()
button = tk.Button(text="User Login")
button.pack()
 
tk.mainloop()