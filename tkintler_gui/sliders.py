from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root =Tk()
root.title('Files dialog')
root.geometry("400x400")

def slide():
    mylabel = Label(root ,text = horizontal.get())
    mylabel.pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

vertical = Scale(root , from_ =0 , to = 400)
vertical.pack()

horizontal = Scale(root , from_ =0 , to = 400 , orient = HORIZONTAL)
horizontal.pack()

mylabel = Label(root ,text = horizontal.get())
mylabel.pack()

my_btn = Button(root , text="Click me" , command =slide).pack()
root.mainloop()