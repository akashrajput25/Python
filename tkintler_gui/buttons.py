#using GRID System , positioning
from tkinter import *

root = Tk()
def myClick():
    mLabel = Label(root, text ="Hi you clicked!")
    mLabel.pack()

#myButton = Button(root ,text="Click me",padx =50, pady=10 ,state=DISABLED).pack()  #creating a button
myButton = Button(root ,text="Click me",padx =50, pady=10, command=myClick, fg="#fff" ,bg = "red").pack()
root.mainloop()