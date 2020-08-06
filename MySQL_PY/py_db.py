import mysql.connector
mydb = mysql.connector.connect(host = "127.0.0.1" , user = "root" , passwd = "password123")

print(mydb)

if(mydb):
    print("Connection Successful")

else:
    print("Connection Unsuccessful")