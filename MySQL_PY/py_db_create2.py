import mysql.connector
mydb = mysql.connector.connect(host ="localhost" , user ="root" ,passwd = "password123" , database ="akashdb")

mycursor = mydb.cursor()

mycursor.execute("Create table employee(name varchar(200) , sal int(20))")