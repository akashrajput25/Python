from tkinter import *
from MySQLdb import *
from Tinkler_switch import *
def ok():

    conobj = connect('localhost','root','password123')
    curobj = conobj.cursor()
    #curobj.execute('Create database GUI_APP;')
    curobj.execute('use GUI_APP;')
    #curobj.execute('create table signup(uname varchar(20),eid varchar(20),var varchar(10),pwd varchar(30));')
    name = uname.get()
    email =eid.get()
    gender = var.get()
    password = pwd.get()
    
    if curobj.execute('insert into signup values("' +uname.get()+ '","' +eid.get()+ '","' +var.get()+ '","' +pwd.get()+ '");') :
        Label(win , text = "Thanks for signing up, now login", font=('bold',10),fg='blue').pack()
    curobj.close()
    conobj.close()

def exit():
    win.destroy()

win = Tk()
win.configure(bg = '#cccccc')
win.title('GUI Application')
win.iconbitmap('C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/ar.ico')

Label(win , text ="     Signup here to Continue!     ",font = ('bold',12),fg='red',bg = '#cccccc').pack(padx=20,pady=10)
f1= Frame()
Label(f1 , text = "User Name :", font=('bold',10),fg='blue').pack(side =LEFT)
uname = Entry(f1 ,font =('bold',9),bg ='#878283', borderwidth = 2,fg='white')
uname.pack(side = RIGHT,padx=10,pady=10)
uname.insert(0,"enter your name")
f1.pack()

f2= Frame()
Label(f2 , text = "Email         :", font=('bold',10),fg='blue').pack(side =LEFT)
eid = Entry(f2 ,font =('bold',9),bg ='#878283', borderwidth = 2,fg='white')
eid.pack(side = RIGHT,padx=10,pady=10)
eid.insert(0,"enter your email")
f2.pack()

f3=Frame()
Label(f3,text='Select Gender', font=('bold',10),fg='blue').pack(side =LEFT,pady=10)
var = StringVar()
r1 =Radiobutton(f3,text='Male',value ='male',variable=var).pack(side = RIGHT)
r2 = Radiobutton(f3,text='female',value = 'female',variable=var).pack(side=RIGHT)
f3.pack()

f4= Frame()
Label(f4 , text = "Password     :", font=('bold',10),fg='blue').pack(side =LEFT,pady=10)
pwd = Entry(f4 ,font =('bold',9),bg ='#878283', borderwidth = 2,fg='white',show='*')
pwd.pack(side = RIGHT)
pwd.insert(0,"enterdsdsdsds")
f4.pack()

f5= Frame()
b1 = Button(f5 , text='Submit',padx=30,bg='#cccccc',command = ok).pack(side = LEFT,padx=5,pady=10)
b2 = Button(f5 , text ='Exit',padx=40,bg='#fccccc',command = exit).pack(side = RIGHT,padx=5,pady=10)
f5.pack()

f6= Frame()
Label(f6 , text = "Already Signed Up , Login here", font=('bold',10),fg='purple',bg = '#cccccc').pack(pady=10)
b3 = Button(f6 , text ='Login',padx=40,bg='#de0d45',fg='#fff',command = login,activebackground = '#21b3db').pack(pady=10)

f6.pack()

win.mainloop()

