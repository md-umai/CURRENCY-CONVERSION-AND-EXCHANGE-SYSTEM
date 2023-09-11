import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root")


mycursor = mydb.cursor()

#mycursor.execute('create database imamdb')


mycursor.execute('Show databases')

for x in mycursor:
    print(x)
