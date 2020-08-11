#using GRID System , positioning
from tkinter import *

root =Tk()

myLabel1 = Label(root , text="Hello World").grid(row=0 ,column = 0) # positioning on screen and creating a label widget
myLabel2 = Label(root , text="Its Akash").grid(row=2 ,column = 1)

root.mainloop()