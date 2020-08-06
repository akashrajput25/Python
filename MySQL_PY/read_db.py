import mysql.connector
mydb = mysql.connector.connect(host ="localhost" , user ="root" ,passwd = "password123" , database ="akashdb")

mycursor = mydb.cursor()

sqlform = "Insert into employee(name , sal) values (%s , %s)"

employees = [("harshit" , 20000) , ("amit" , 30000) , ("akash" , 11000), ]

mycursor.executemany(sqlform , employees)

mydb.commit()