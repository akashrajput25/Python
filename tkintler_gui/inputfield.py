from tkinter import *

root = Tk()

e = Entry(root, borderwidth = 4 )
e.pack()
e.insert(0,"enter your name")

def myClick():
    mLabel = Label(root, text ="Hello " + e.get())
    mLabel.pack()

#myButton = Button(root ,text="Click me",padx =50, pady=10 ,state=DISABLED).pack()  #creating a button
myButton = Button(root ,text="submit",padx =50, pady=10, command=myClick, fg="#fff" ,bg = "red").pack()
root.mainloop()