from tkinter import *
from PIL import ImageTk, Image

root =Tk()

root.title('Create new window')


def open():
    global my_img
    top = Toplevel()
    top.title('image window')
    my_img = ImageTk.PhotoImage(Image.open("C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/soa.png"))
    my_label = Label(top , image = my_img).pack()
    btn2 = Button(top , text ="close window" , command= top.destroy).pack()

btn = Button(root , text ='open second window', command = open).pack()
root.mainloop()