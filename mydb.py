import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='#Rishi123',
)

# prepare a cursor object
cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE shobhitco")
print("All done!!")