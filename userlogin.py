import tkinter as tk
#PrintLogger code from Quora
"""class PrintLogger: 
    def __init__(self, textbox): 
        self.textbox = textbox 
 
    def write(self, text): 
        self.textbox.insert(tk.END, text) 
 
root = tk.Tk() 
 
textbox = tk.Text(root) 
textbox.pack() 
 
printlogger = PrintLogger(textbox) 
sys.stdout = printlogger""" 
class Userinfo:
    def __init__(self, name, highscore):
        self.name = name
        self.highscore = highscore
def login():
    TKWindow = tk.TK()
    TKWindow.geometry('300x300')
    usernameLabel = Label(tkWindow, text="Choose your username")
    usernameLabel.pack()
    usernameEntry = Entry(tkWindow, textvariable=username)
    usernameEntry.pack()

mainWindow = tk()
mainWindow.geometry('300x300')
hello = tk.Label(text="Welcome to the spelling game!")
hello.pack()
userbutton = tk.Button(text="User Login", 
                   command=login)
userbutton.pack()
 
tk.mainloop()

    