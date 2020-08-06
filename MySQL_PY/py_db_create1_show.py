import mysql.connector
mydb = mysql.connector.connect(host ="localhost" , user ="root" ,passwd = "password123" , database ="akashdb")

mycursor = mydb.cursor()

mycursor.execute("Show tables")

for tb in mycursor:
    print(tb)