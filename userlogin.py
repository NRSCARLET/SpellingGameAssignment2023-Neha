import sys 
import tkinter as tk 
class PrintLogger: 
    def __init__(self, textbox): 
        self.textbox = textbox 
 
    def write(self, text): 
        self.textbox.insert(tk.END, text) 
 
root = tk.Tk() 
 
textbox = tk.Text(root) 
textbox.pack() 
 
printlogger = PrintLogger(textbox) 
sys.stdout = printlogger 
 
# print("Hello, world!")  # This will appear in the Text widgetroot.mainloop()

window = tk.Tk()
window.title("Button Speller")
window.geometry("300x300")

hello = tk.Label(text="Welcome to the spelling game!")
hello.pack()

def login():
    print("Hello Tester")


userbutton = tk.Button(text="User Login", 
                   command=login)
userbutton.pack()
 
tk.mainloop()
class Userlogin:
    def __init__(self, name, highscore):
        self.name = name
        self.highscore = highscore


    