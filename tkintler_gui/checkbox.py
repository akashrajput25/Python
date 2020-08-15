from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title('Image Viewer')
root.geometry('400x400')

def clicked():
    mylabel = Label(root , text = var.get()).pack()

var = StringVar()

c = Checkbutton(root , text ="Check" , variable = var,onvalue ="on",offvalue ="off")
c.deselect()
c.pack()

mybutton = Button(root , text ="show selection", command= clicked).pack()

root.mainloop()