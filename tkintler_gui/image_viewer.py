from tkinter import *
from PIL import ImageTk,Image

root =Tk()
root.title('Basics icon, img and cross btn')
root.iconbitmap('C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/ar.ico')

my_img1 = ImageTk.PhotoImage(Image.open('C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/soa.png'))
my_img2 = ImageTk.PhotoImage(Image.open('C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/js.png'))
my_img3 = ImageTk.PhotoImage(Image.open('C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/c.png'))
my_img4 = ImageTk.PhotoImage(Image.open('C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/java.png'))
my_img5 = ImageTk.PhotoImage(Image.open('C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/github.png'))

img_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

my_Label = Label(image = my_img1)
my_Label.grid(row = 0 , column = 0 ,columnspan =3)

def next(image_no):
    global my_Label
    global button_next
    global button_back

    my_Label.grid_forget()
    my_Label = Label(image = img_list[image_no-1])
    button_next = Button(root,text ='>>' , command = lambda:next(image_no+1))
    button_back = Button(root,text ='<<' , command = lambda:back(image_no-1))
    
    if image_no == 5:
        button_next = Button(root,text='>>',state = DISABLED)
    my_Label.grid(row = 0 , column = 0 ,columnspan =3)
    button_back.grid(row=1 , column = 0)
    button_next.grid(row =1 , column = 2)

def back(image_no):
    global my_Label
    global button_next
    global button_back

    my_Label.grid_forget()
    my_Label = Label(image = img_list[image_no-1])
    button_next = Button(root,text ='>>' , command = lambda:next(image_no+1))
    button_back = Button(root,text ='<<' , command = lambda:back(image_no-1))
    
    
    if image_no == 1:
        button_back = Button(root,text='<<',state = DISABLED)
    my_Label.grid(row = 0 , column = 0 ,columnspan =3)
    button_back.grid(row=1 , column = 0)
    button_next.grid(row =1 , column = 2)

button_back = Button(root,text = "<<", command = back ,state= DISABLED)
button_next = Button(root,text = ">>", command = lambda: next(2))
button_exit = Button(root,text = "Exit program",command = root.quit)

button_back.grid(row=1 , column = 0)
button_exit.grid(row =1 , column = 1)
button_next.grid(row =1 , column = 2)

root.mainloop()