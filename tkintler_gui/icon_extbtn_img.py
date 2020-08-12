from tkinter import *
from PIL import ImageTk,Image

root =Tk()
root.title('Basics icon, img and cross btn')
root.iconbitmap('C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/ar.ico')

my_img = ImageTk.PhotoImage(Image.open('C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/soa.png'))
my_Label = Label(image = my_img)
my_Label.pack()


button_quit = Button(root , text ='Exit Program', command = root.quit)
button_quit.pack()
root.mainloop()