import mysql.connector
import datetime
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="imamdb")

x=datetime.datetime.now()
mycursor = mydb.cursor()

mycursor.execute('INSERT INTO currencyconvert(uid,basecurrency,convertcurrency,baseamount,convertedamount,datetime) VALUES(%s,%s,%s,%s,%s,%s)',(1040343,"us dollars","indian rupees",200.0,15133.45,x))
mydb.commit()
