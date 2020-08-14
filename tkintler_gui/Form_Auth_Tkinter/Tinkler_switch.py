from tkinter import *
from MySQLdb import *
def login():
    win1 = Tk ()
    win1.configure(bg = '#cccccc')
    win1 . title ( 'Please login here')

    def submit():
        conobj =connect(host='localhost',user='root',password='password123',database='GUI_APP')
        curobj = conobj.cursor()
        curobj.execute('use GUI_APP;')
        curobj.execute("SELECT uname, pwd FROM signup")
        signup = curobj.fetchall()
        print(signup)
        #curobj.execute('Create database GUI_APP;')

        name = uname.get()
        password = pwd.get()

        for data in signup:
            
            if str(data[0]) == name and str(data[1]) == password:
                Label(win1 , text ="Thank you for logging in",font = ('bold',12),fg='#fff',bg = '#fff').grid(row = 11, column =0)
        
        curobj.close()
        conobj.close()

    def exit():
        win1.destroy()

    Label(win1 , text ="Login here to your account!",font = ('bold',12),fg='red',bg = '#cccccc').grid(row=0 ,column=0,padx=20,pady=10)
    win1.iconbitmap('C://Users/AKASH RAJPUT/Desktop/Python/tkintler_gui/ar.ico')
    
    mylabel=Label(win1 , text = "Enter User Name :", font=('bold',11),fg='blue',bg = '#cccccc').grid(row=1 ,column=0)
    uname = Entry(win1 ,font =('bold',9),bg ='#c0c0c0',fg='white', borderwidth = 2)
    uname.grid(row=1 ,column=1,padx=10,pady=10)

    mylabel = Label(win1 , text = "Enter Password :", font=('bold',11),fg='blue',bg = '#cccccc').grid(row=4 ,column=0)
    pwd = Entry(win1 ,font =('bold',9),bg ='#c0c0c0',fg='white',show='*', borderwidth = 2)
    pwd.grid(row=4 ,column=1,padx=10,pady=10)

    sbtn = Button(win1 , text='Submit',padx=45,bg='#cccccc',command = submit).grid(row=10 ,column=0, pady=20)
    ebtn = Button(win1 , text ='Exit',padx=60,bg='#fccccc',command = exit).grid(row=10 ,column=1, pady=20)
    
    win1. mainloop ()
