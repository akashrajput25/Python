from tkinter import *

def popout():
    win2 = Tk ()
    win2.geometry('400x70')
    win2.configure(bg = '#cccccc')
    labelframe = LabelFrame(win2 , text = "X-Company")
    Label(labelframe , text ="Thank you for logging in",font = ('bold',12),fg='#008000').pack()
    Label(labelframe , text ="Welcome to X Company",font = ('bold',12),fg='#008000').pack()
    labelframe.pack()