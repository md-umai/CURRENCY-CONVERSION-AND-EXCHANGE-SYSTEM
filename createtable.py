import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="imamdb")


mycursor = mydb.cursor()

#mycursor.execute('create table currencyconvert (id int PRIMARY KEY AUTO_INCREMENT,uid int(30),basecurrency varchar(50),convertcurrency varchar(50),baseamount float,convertedamount float,datetime varchar(50))')

mycursor.execute('DESCRIBE currencyconvert')

for x in mycursor:
    print(x)