import mysql.connector
mydb = mysql.connector.connect(host ="localhost" , user ="root" ,passwd = "password123" , database ="akashdb")

mycursor = mydb.cursor()

sql = "DELETE FROM employee WHERE name ='akash'"

mycursor.execute(sql)

mydb.commit()