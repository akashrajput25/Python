from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root =Tk()
root.title('message box')

def popup():
    #messagebox.showinfo("This is popup","Hello World")
    #messagebox.showwarning("This is popup","Hello World")
    #messagebox.showerror("This is popup","Hello World")
    #messagebox.askquestion("This is popup","Hello World")
    #messagebox.askokcancel("This is popup","Hello World")
    response = messagebox.askyesno("This is popup","Hello World")
    if response == 1:
        response ='yes'
        Label(root , text =response).pack()

    else:
        response ='no'
        Label(root , text =response).pack()

Button(root,text = "Popup" , command = popup).pack()

root.mainloop()