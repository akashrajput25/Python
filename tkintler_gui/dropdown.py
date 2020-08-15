from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title('Image Viewer')
root.geometry('400x400')

def show():
    mylabel = Label(root , text =clicked.get()).pack()

options = ["Mon","Tues","Wed","Fri","Sat"]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root , clicked , *options)
drop.pack()

mybtn = Button(root , text="show selection" , command =show).pack()
root.mainloop()