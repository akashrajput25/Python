from tkinter import *

root =Tk()

root.title('Frames')

#r = IntVar()
#r.set('2')

TOPPINGS = [("pepper","pepper"),("cheese","cheese"),("mushroom","mushroom"),("onion","onion")]

pizza = StringVar()
pizza.set('pepper')

for text,topping in TOPPINGS:
    Radiobutton(root,text =text, variable=pizza,value =topping).pack(anchor = W)

def clicked(value):
   MyLabel = Label(root , text = value)
   MyLabel.pack() 

#Radiobutton(root , text ='option1',variable = r ,value =1, command =lambda :clicked(r.get())).pack()
#Radiobutton(root , text ='option2',variable = r ,value =2, command =lambda :clicked(r.get())).pack()

#MyLabel = Label(root , text = pizza.get())
#MyLabel.pack()

mybtn = Button(root,text='click',command=lambda: clicked(pizza.get()))
mybtn.pack()
root.mainloop()