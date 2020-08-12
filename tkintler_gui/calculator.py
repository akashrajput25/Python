from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root,width =35, borderwidth = 4 )
e.grid(row=0 ,column=0, columnspan = 3,padx=10 ,pady=10)
#e.insert(0,"enter your name")

def button_click(number):
    #e.delete(0 , END)
    current = e.get()
    e.delete(0 , END)
    e.insert(0 , str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num 
    global math 
    math ='add'
    f_num = int(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = 'subtract' 
    f_num = int(first_number)
    e.delete(0,END)

def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = 'multiply' 
    f_num = int(first_number)
    e.delete(0,END)

def button_div():
    first_number = e.get()
    global f_num
    global math 
    math = 'divide'
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number =e.get()
    e.delete(0,END)

    if math == 'add':
        e.insert(0,f_num + int(second_number))

    if math == 'subtract':
        e.insert(0,f_num - int(second_number))

    if math == 'multiply':
        e.insert(0,f_num * int(second_number))

    if math == 'divide':
        e.insert(0,f_num / int(second_number))

button_1 = Button(root,text ='1' , padx=40,pady=20 ,activebackground ='#c0c0c0', command= lambda: button_click(1))
button_2 = Button(root,text ='2' , padx=40,pady=20 ,activebackground ='#c0c0c0', command= lambda: button_click(2))
button_3 = Button(root,text ='3' , padx=40,pady=20 ,activebackground ='#c0c0c0', command= lambda: button_click(3))
button_4 = Button(root,text ='4' , padx=40,pady=20 ,activebackground ='#c0c0c0', command= lambda: button_click(4))
button_5 = Button(root,text ='5' , padx=40,pady=20 ,activebackground ='#c0c0c0', command= lambda: button_click(5))
button_6 = Button(root,text ='6' , padx=40,pady=20 ,activebackground ='#c0c0c0', command= lambda: button_click(6))
button_7 = Button(root,text ='7' , padx=40,pady=20 ,activebackground ='#c0c0c0', command= lambda: button_click(7))
button_8 = Button(root,text ='8' , padx=40,pady=20 ,activebackground ='#c0c0c0', command= lambda: button_click(8))
button_9 = Button(root,text ='9' , padx=40,pady=20 ,activebackground ='#c0c0c0', command= lambda: button_click(9))
button_0 = Button(root,text ='0' , padx=40,pady=20 ,activebackground ='#c0c0c0', command= lambda: button_click(0))
button_add= Button(root,text ='+' , padx=39,pady=20 ,activebackground ='#c98f06', command= button_add)
button_sub= Button(root,text ='-' , padx=40.5,pady=20 ,activebackground ='#c98f06', command= button_sub)
button_mul= Button(root,text ='*' , padx=40.4,pady=20 ,activebackground ='#c98f06', command= button_mul)
button_div= Button(root,text ='/' , padx=40.8,pady=20 ,activebackground ='#c98f06', command= button_div)
button_equal = Button(root,text ='=' , padx=133.5,pady=20 ,activebackground='#0752f2', command= button_equal)
button_clear = Button(root,text ='Clear' , padx=29.5,pady=20 ,activebackground='#0752f2', command= button_clear)

#putting button on the screen
button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)
button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)
button_7.grid(row= 1,column=0)
button_8.grid(row= 1,column=1)
button_9.grid(row= 1,column=2)
button_0.grid(row= 4,column=0)
button_add.grid(row=4 , column=1)
button_sub.grid(row=4 , column=2)
button_mul.grid(row=5 , column=0)
button_div.grid(row=5 , column=1)
button_clear.grid(row=5,column=2)
button_equal.grid(row=6,column=0,columnspan=3)
#myButton = Button(root ,text="Click me",padx =50, pady=10 ,state=DISABLED).pack()  #creating a button

root.mainloop()