import mysql.connector 

dataBase=mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "shiv@760",
)

#prepare cursor object
cursorObject = dataBase.cursor()
#create a database 
cursorObject.execute("CREATE DATABASE crm")

print("All done!")