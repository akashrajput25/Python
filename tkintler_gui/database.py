from tkinter import *
from PIL import Image,ImageTk
import sqlite3

root = Tk()
root.title('Address Book')
root.geometry('400x500')

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
f_name.grid(row =0 , column =1,padx=20 , pady =(20,0))

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
delete_box = Entry(root , width =30)
delete_box.grid(row =9 , column =1 ,pady=(25,5))

#create text box labels

f_name_label =Label(root,text ="First Name")
f_name_label.grid(row = 0, column = 0 , pady =(20,0))

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

delete_box_label = Label(root , text="Select ID" )
delete_box_label.grid(row =9 , column =0 , pady =(25,5))

#update function
def update():
     #creating a database 
    conn = sqlite3.connect('address_book.db')

    #creating a cursor object
    cur = conn.cursor()

    record_id = delete_box.get()
    cur.execute("""UPDATE addresses SET
        first_name =:first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode =:zipcode

        WHERE oid = :oid""",

        {
        'first': f_name_editor.get(),
        'last' : l_name_editor.get(),
        'address' : address_editor.get(),
        'city' : city_editor.get(),
        'state' : state_editor.get(),
        'zipcode' : zipcode_editor.get(),
        'oid' : record_id
        })

    #commiting all the changes
    conn.commit()

    #close the connection
    conn.close()   

    editor.destroy()

#edit function to update record
def edit():
    global editor
    editor = Tk()
    editor.title('Update Record')
    editor.geometry('400x200')

    #create global variables
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    #creating a database 
    conn = sqlite3.connect('address_book.db')

    #creating a cursor object
    cur = conn.cursor()   
    
    record_id = delete_box.get()

    #Query the database
    cur.execute("SELECT * FROM addresses WHERE oid = "+ record_id)
    records = cur.fetchall()
    
    #Create Text Boxes
    f_name_editor = Entry(editor,width =30)
    f_name_editor.grid(row =0 , column =1,padx=20 , pady =(20,0))

    l_name_editor = Entry(editor,width =30)
    l_name_editor.grid(row =1 , column =1,padx=20)

    address_editor = Entry(editor,width =30)
    address_editor.grid(row =2 , column =1,padx=20)

    city_editor = Entry(editor,width =30)
    city_editor.grid(row =3 , column =1,padx=20)

    state_editor = Entry(editor,width =30)
    state_editor.grid(row =4, column =1,padx=20)

    zipcode_editor = Entry(editor,width =30)
    zipcode_editor.grid(row =5 , column =1,padx=20)

    #create text box labels

    f_name_label =Label(editor,text ="First Name")
    f_name_label.grid(row = 0, column = 0 , pady =(20,0))

    l_name_label =Label(editor,text ="Last Name")
    l_name_label.grid(row = 1, column = 0)

    address_label =Label(editor,text ="Address")
    address_label.grid(row = 2, column = 0)

    city_label =Label(editor,text ="City")
    city_label.grid(row = 3, column = 0)

    state_label =Label(editor,text ="State")
    state_label.grid(row = 4, column = 0)

    zipcode_label =Label(editor,text ="Zip Code")
    zipcode_label.grid(row =5, column = 0)

    #Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    #Create a save editted value button
    save_btn =Button(editor,text="Save Record",command=update)
    save_btn.grid(row=11 , column =0 , columnspan =2 ,pady=10 , padx =10 ,ipadx =155)


#create functn to delete a record
def delete():
    #creating a database 
    conn = sqlite3.connect('address_book.db')

    #creating a cursor object
    cur = conn.cursor() 

    cur.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    delete_box.delete(0, END)

    #commiting all the changes
    conn.commit()

    #close the connection
    conn.close()

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
        print_records += str(record[0]) +" "+ str(record[1]) +"    "+str(record[6])+"\n"
    query_label = Label(root , text = print_records)
    query_label.grid(row =12 , column =0 ,columnspan =2)

    #commiting all the changes
    conn.commit()

    #close the connection
    conn.close()

#Create submit button
Submit_btn = Button(root, text ="add record to Database" , command =submit)
Submit_btn.grid(row=6 , column=0 , columnspan =2 , pady=10 , padx=10 , ipadx=125)

#create a query button
query_btn =Button(root,text="show record",command=query)
query_btn.grid(row=7 , column =0 , columnspan =2,pady=10 , padx =10 ,ipadx =153)

#create a delete button
delete_btn =Button(root,text="Delete Record",command=delete)
delete_btn.grid(row=10 , column =0 , columnspan =2 ,pady=10 , padx =10 ,ipadx =149)

#Create an edit button
edit_btn =Button(root,text="Edit Record",command=edit)
edit_btn.grid(row=11 , column =0 , columnspan =2 ,pady=10 , padx =10 ,ipadx =155)

#commiting all the changes
conn.commit()

#close the connection
conn.close()

root.mainloop()