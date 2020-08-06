import mysql.connector
mydb = mysql.connector.connect(host ="localhost" , user ="root" ,passwd = "password123")

mycursor = mydb.cursor()
mycursor.execute("Show databases")

for db in mycursor:
    print(db)
