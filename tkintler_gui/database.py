from tkinter import *
from PIL import Image,ImageTk
import sqlite3

root = Tk()
root.title('Address Book')
root.geometry('400x400')

#Database
#creating a database 
conn = sqlite3.connect('address_book.db')

#creating a cursor object
cur = conn.cursor()

'''
#create a table
cur.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    ) """)
'''

#Create Text Boxes
f_name = Entry(root,width =30)
f_name.grid(row =0 , column =1,padx=20)

l_name = Entry(root,width =30)
l_name.grid(row =1 , column =1,padx=20)

address = Entry(root,width =30)
address.grid(row =2 , column =1,padx=20)

city = Entry(root,width =30)
city.grid(row =3 , column =1,padx=20)

state = Entry(root,width =30)
state.grid(row =4, column =1,padx=20)

zipcode = Entry(root,width =30)
zipcode.grid(row =5 , column =1,padx=20)

#create text box labels

f_name_label =Label(root,text ="First Name")
f_name_label.grid(row = 0, column = 0)

l_name_label =Label(root,text ="Last Name")
l_name_label.grid(row = 1, column = 0)

address_label =Label(root,text ="Address")
address_label.grid(row = 2, column = 0)

city_label =Label(root,text ="City")
city_label.grid(row = 3, column = 0)

state_label =Label(root,text ="State")
state_label.grid(row = 4, column = 0)

zipcode_label =Label(root,text ="Zip Code")
zipcode_label.grid(row =5, column = 0)

#Submit functn for database
def submit():
    #creating a database 
    conn = sqlite3.connect('address_book.db')

    #creating a cursor object
    cur = conn.cursor()   
    
    #insert into table
    cur.execute("INSERT INTO addresses VALUES (:f_name , :l_name, :address ,:city ,:state ,:zipcode)",
        {
            'f_name':f_name.get(),
            'l_name':l_name.get(),
            'address':address.get(),
            'city':city.get(),
            'state':state.get(),
            'zipcode':zipcode.get()
        })

    #commiting all the changes
    conn.commit()

    #close the connection
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#create query functn
def query():
    #creating a database 
    conn = sqlite3.connect('address_book.db')

    #creating a cursor object
    cur = conn.cursor()   
    
    #Query the database
    cur.execute("SELECT *,oid FROM addresses"),
    records = cur.fetchall()

    print_records=''
    #Loop through the records
    for record in records:
        print_records +="Name = "+ str(record[0]) +" "+ str(record[1]) + "\n" +"address = "+str(record[2])+"\n"
        print_records +="\n"
    query_label = Label(root , text = print_records)
    query_label.grid(row = 8 , column =0 ,columnspan =2)

    #commiting all the changes
    conn.commit()

    #close the connection
    conn.close()

#Create submit button
Submit_btn = Button(root, text ="add record to Database" , command =submit)
Submit_btn.grid(row=6 , column=0 , columnspan =2 , pady=10 , padx=10 , ipadx=100)

#create a query button
query_btn =Button(root,text="show record",command=query)
query_btn.grid(row=7 , column =0 , columnspan =2 ,pady=10 , padx =10 ,ipadx =129)
#commiting all the changes
conn.commit()

#close the connection
conn.close()

root.mainloop()