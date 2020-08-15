from tkinter import *
from PIL import Image,ImageTk
import sqlite3

root = Tk()
root.title('Image Viewer')
root.geometry('400x400')

#Database
#creating a database 
conn = sqlite3.connect('address_book.db')

#creating a cursor object
cur = conn.cursor()

#create a table
cur.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    ) """)

#commiting all the changes
conn.commit()

#close the connection
conn.close()

root.mainloop()