from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root =Tk()

root.title('Files dialog')


def open():
    global myimage
    root.filename = filedialog.askopenfilename(initialdir  = 'C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/' , title ='select file' , filetypes = (('png files','*.png'),('all files','*.*')))
    mylabel = Label(root , text =root.filename).pack()
    myimage = ImageTk.PhotoImage(Image.open(root.filename))
    myimagelabel = Label(image = myimage).pack()

mybtn = Button(root , text ='open file', command = open).pack()

root.mainloop()